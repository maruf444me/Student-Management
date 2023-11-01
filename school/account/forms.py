from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.db import transaction
from .models import User, Student, Teacher, StudentProfile, TeacherProfile



# ======================================================
#               Form For Student Registration
# ======================================================
class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=233, required=True, widget=forms.EmailInput(attrs={'class': 'form-control'},),
        label='Email', label_suffix=' ', error_messages= {'required': 'Enter Your Email'},
     )
    roll = forms.CharField(
        max_length=100, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'},),
        label='Roll', label_suffix=' ', error_messages= {'required': 'Enter Your Roll'},
        )
    registration = forms.CharField(
        max_length=300, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'},),
        label='Registration', label_suffix=' ', error_messages= {'required': 'Enter Your Registration'},                           
    )
    department = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'},),
        label='Department', label_suffix=' ', error_messages= {'required': 'Enter Your Department'},
    )
    password1 = forms.CharField(
        max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'},),
        label='Password', label_suffix=' ', error_messages= {'required': 'Enter Your Password'},
    )
    password2 = forms.CharField(
        max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'},),
        label='Password (confirm)', label_suffix=' ', error_messages= {'required': 'Enter Your Confirm Password'},
    )
    username = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'},),
        label='Username', label_suffix=' ', error_messages= {'required': 'Enter Your Username'},
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # labels = {
        #     'username': 'Username',
        #     }
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'},),
        # }
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.roll = self.cleaned_data.get('roll')
        student.registration = self.cleaned_data.get('registration')
        student.department = self.cleaned_data.get('department')
        student.save()
        return user
# ====================== End Form =======================



# ======================================================
#           Student Profile Information Add 
# ======================================================
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ['user']
        widgets = {
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }  
# ====================== End Form =======================


# ======================================================
#               Form For Student Registration
# ======================================================
class TeacherRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=233, required=True, widget=forms.EmailInput(attrs={'class': 'form-control'},),
        label='Email', label_suffix=' ', error_messages ={'required': 'Enter Your Email'},)
    department = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'},),
        label='Department', label_suffix=' ', error_messages ={'required': 'Enter Your Department'},)
    password1 = forms.CharField(
        max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'},),
        label='Password', label_suffix=' ', error_messages ={'required': 'Enter Your Password'},)
    password2 = forms.CharField(
        max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'},),
        label='Password (confirm)', label_suffix=' ', error_messages ={'required': 'Enter Your Confirm Password'},)
    username = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'},),
        label='Username', label_suffix=' ', error_messages ={'required': 'Enter Your Username'},)

    class Meta(UserCreationForm.Meta):
        model = User
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'},),
        # }
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.department = self.cleaned_data.get('department')

        teacher.save()
        return user
# ====================== End Form =======================



# ======================================================
#           Student Profile Information Add 
# ======================================================
class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        exclude = ['user']
        widgets = {
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'rank': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.TextInput(attrs={'class': 'form-control'}),
        } 
# ====================== End Form =======================



# ======================================================
#               Form For Student/Teacher Login 
# ======================================================
class TeacherStudentLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'},),
        label='Username', label_suffix=' ', error_messages= {'required': 'Please Enter Your Username'},
        )
    password = forms.CharField(
        max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'},),
        label='Email', label_suffix=' ', error_messages= {'required': 'Please Enter Your Email'},
        )
# ====================== End Form =======================



# ======================================================
#               Password Change for Teacher/Student 
# ======================================================
class TeacherStudentPasswordChangedForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label_suffix= ' ', error_messages={'required': 'Enter Your Old Password'})
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label_suffix= ' ', label='New Password', error_messages={'required': 'Enter Your New Password'})
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label_suffix= ' ', label='New Password (confirm)', error_messages={'required': 'Enter Your Confirm Password'})

# ====================== End Form =======================