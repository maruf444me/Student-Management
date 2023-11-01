from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import TeacherProfile
from .form import AddStudentForm, StudentUpdateData 
from .models import StudentDetail




# ============================================================
#           Function For Teacher Home Page
# ============================================================
def teacher_home(request):
    return render(request, 'teacher/teacher_home.html')
# ===================== End Function =========================

# ============================================================
#           Function For Add Student Details
# ============================================================
@login_required
def add_student(request):
    if request.method == 'POST':
        fm = AddStudentForm(request.POST, request.FILES, label_suffix= ' ')
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Studet data added Successfully')
            return redirect('show_student_detail')
    else:
        fm = AddStudentForm(label_suffix= '')
    return render(request, 'teacher/student_details/add_student.html', {'form': fm})
# ===================== End Function =========================




# ============================================================
#           Function For Show Student Details
# ============================================================
@login_required 
def show_student_detail(request):
    fm = StudentDetail.objects.all()
    return render(request, 'teacher/student_details/show_student_data.html', {'stu_info': fm})
# ===================== End Function =========================


# ============================================================
#           Function For Show Student Details
# ============================================================
@login_required 
def show_student_more_detail(request, id):
    fm = StudentDetail.objects.get(pk=id)
    return render(request, 'teacher/student_details/show_more.html', {'stu_info': fm})
# ===================== End Function =========================


# ============================================================
#           Function For  Student Update Details
# ============================================================
@login_required 
def update_student_data(request, id):
    pk = StudentDetail.objects.get(pk=id)
    if request.method == 'POST':
        update_data = StudentUpdateData(request.POST, request.FILES, instance=pk, label_suffix= '')
        if update_data.is_valid():
            update_data.save()
            return redirect('show_student_detail')
            
    else:
        update_data = StudentUpdateData(instance=pk, label_suffix= ' ')
    return render(request, 'teacher/student_details/student_update.html', {'form': update_data})
# ===================== End Function =========================



# ============================================================
#           Function For  Student delete Details
# ============================================================
@login_required 
def delate_student_data(request, id):
    if request.method == 'POST':
        data = StudentDetail.objects.get(pk=id)
        data.delete()
    return redirect('teacher/student_details/show_student_detail')
# ===================== End Function =========================


# ============================================================
#           Function For  Teacher Dashbord
# ============================================================
@login_required 
def teacher_dashbord(request):
    user = request.user
    try:
        teacher_profile = TeacherProfile.objects.get(user=user)
    except TeacherProfile.DoesNotExist:
        teacher_profile = None

    context = {'teacher_profile': teacher_profile}
    
    return render(request, 'teacher/dashbord.html', context) 
# ===================== End Function =========================

