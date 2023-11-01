from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from teacher.models import TeacherVerify
from .models import User, TeacherProfile, StudentProfile
from .forms import StudentRegistrationForm, TeacherRegistrationForm, TeacherStudentLoginForm, StudentProfileForm, TeacherProfileForm, TeacherStudentPasswordChangedForm

# ======================================================
#               Class For Student Registration
# ======================================================
class StudentRegister(CreateView):
    model = User
    form_class = StudentRegistrationForm
    template_name = 'account/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Your account created successfully! Now login')
        return redirect('login')
 # ====================== End Class =======================



# ======================================================
#               Class For Student Profile
# ======================================================
@login_required
def student_profile(request):
    user = request.user
    has_profile = StudentProfile.objects.filter(user=user).exists()

    if request.method == 'POST':
        if has_profile:
            profile = StudentProfile.objects.get(user=user)
            fm = StudentProfileForm(request.POST, request.FILES, instance=profile)
        else:
            fm = StudentProfileForm(request.POST, request.FILES)

        if fm.is_valid():
            profile = fm.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('student_dashbord')

    elif has_profile:
        profile = StudentProfile.objects.get(user=user)
        fm = StudentProfileForm(instance=profile)
    else:
        fm = StudentProfileForm()
    return render(request, 'account/student_profile.html', {'form': fm})
# ====================== End =======================



# ======================================================
#               Class For Teacher Registration
# ======================================================
class TeacherRegister(CreateView):
    model = User
    form_class = TeacherRegistrationForm
    template_name = 'account/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Your account created successfully! Now login')
        return redirect('login')
# ====================== End Class =======================




# ======================================================
#               Function For Teacher/Student Login
# ======================================================
def teacher_student_login(request):
    if request.method == 'POST':
        fm = TeacherStudentLoginForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                if user.is_student:
                    login(request, user)
                    messages.success(request, 'Login successfully!')
                    return redirect('student_dashbord')
                elif user.is_teacher:
                    login(request, user)
                    messages.success(request, 'Login successfully!')
                    return redirect('teacher_dashbord')
    else:
        fm = TeacherStudentLoginForm()
    return render(request, 'account/login.html', {'form': fm})
# ====================== End =======================



# ======================================================
#               Function For Teacher/Student Login
# ======================================================
@login_required 
def teacher_student_password_changed(request):
    if request.method == 'POST':
        fm = TeacherStudentPasswordChangedForm(request.user, request.POST)
        if fm.is_valid():
            user = fm.save()
            update_session_auth_hash(request, user) 

            if user.is_student:
                messages.success(request, 'Password changed successfully!')
                return redirect('student_dashbord')
            elif user.is_teacher:
                messages.success(request, 'Password changed successfully!')
                return redirect('teacher_dashbord')
    else:
        fm = TeacherStudentPasswordChangedForm(request.user)
    return render(request, 'account/password_change.html', {'form': fm})
# ====================== End =======================



# ======================================================
#               Class For Teacher/Student Logout
# ======================================================
@login_required 
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home_page')
# ====================== End Class =======================


# ======================================================
#               Class For teacher profile
# ======================================================
@login_required
def teacher_profile(request):
    user = request.user
    has_profile = TeacherProfile.objects.filter(user=user).exists()

    if request.method == 'POST':
        if has_profile:
            # User already has a profile, update it
            profile = TeacherProfile.objects.get(user=user)
            fm = TeacherProfileForm(request.POST, request.FILES, instance=profile)
        else:
            fm = TeacherProfileForm(request.POST, request.FILES)

        if fm.is_valid():
            profile = fm.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('teacher_dashbord')

    elif has_profile:
        profile = TeacherProfile.objects.get(user=user)
        fm = TeacherProfileForm(instance=profile)
    else:
        fm = TeacherProfileForm()

    return render(request, 'account/teacher_profile.html', {'form': fm})

# ====================== End Class =======================


# ============================================================
#           Function For  Teacher Verifying
# ============================================================
def teacher_verify(request):
    if request.method == 'POST':
        school = request.POST.get('school')
        pin = request.POST.get('pin')
        try:
            TeacherVerify.objects.get(school_name=school, pin=pin)
        except TeacherVerify.DoesNotExist:
            return redirect('student_register')
        return redirect('teacher_register')

    return render(request, 'account/teacher_verify.html')
# ===================== End Function ========================= 

