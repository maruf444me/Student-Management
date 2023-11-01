from django.urls import path
from .views import StudentRegister, TeacherRegister, teacher_student_login, user_logout, student_profile,teacher_profile,teacher_verify, teacher_student_password_changed


urlpatterns = [
    path('student/', StudentRegister.as_view(), name='student_register'),
    path('teacher/', TeacherRegister.as_view(), name='teacher_register'),
    path('login/', teacher_student_login, name='login'),
    path('logout/', user_logout, name='user_logout'),
    path('student_profile/', student_profile, name='student_profile'),
    path('teacher_profile/', teacher_profile, name='teacher_profile'),
    path('teacher_verify/', teacher_verify, name='teacher_verify'),
    path('password_change/', teacher_student_password_changed, name='password_change'),
]