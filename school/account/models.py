from django.db import models
from django.contrib.auth.models import AbstractUser

# ======================================================
#                   Base User Model
# ======================================================
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile_picture', null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=200)
    city =  models.CharField(max_length=60)
    email = models.EmailField(max_length=200)
    phone =  models.CharField(max_length=15)
    address =  models.CharField(max_length=500)
    rank = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
# ====================== End Model=======================



# ======================================================
#                   Model For Student
# ======================================================
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    roll = models.CharField(max_length=100)
    registration = models.CharField(max_length=300)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
# ====================== End Model=======================



# ======================================================
#                   Model For Student
# ======================================================
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='student_profile', null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=200)
    city =  models.CharField(max_length=60)
    phone =  models.CharField(max_length=15)
    address =  models.CharField(max_length=500)
# ====================== End Model=======================


# ======================================================
#                   Model For Teacher
# ======================================================
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
# ====================== End Model=======================



# ======================================================
#                   Model For Teacher Profile
# ======================================================
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='teacher_profile', null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=200)
    city =  models.CharField(max_length=60)
    phone =  models.CharField(max_length=15)
    rank = models.CharField(max_length=100)
    address =  models.CharField(max_length=500)
    about = models.TextField()
# ====================== End Model=======================