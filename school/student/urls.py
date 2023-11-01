from django.urls import path
from .views import *



urlpatterns = [
    path('', StudentHomePage.as_view(), name='student_home'),
    path('student_dashbord/', StudentDashbord.as_view(), name='student_dashbord'),
    path('result/', student_result, name='stu_result'),
    path('teacher_info/', teacher_info, name='teacher_info'),

]