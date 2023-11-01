from django.urls import path
from .views import *



urlpatterns = [
    path('', teacher_home, name='teacher_home'),
    # Path For Student Crud Operation
    path('add_student/', add_student, name='add_student'),
    path('show_student_detail/',show_student_detail, name='show_student_detail'),
    path('show_more/<int:id>/', show_student_more_detail, name='show_more'),
    path('update_student_data/<int:id>/', update_student_data, name='update_student_data'),
    path('delete_student_data/<int:id>/', delate_student_data, name='delete_student_data'),
    # Path For Teacher 
    path('teacher_dashbord/', teacher_dashbord, name='teacher_dashbord'),

]