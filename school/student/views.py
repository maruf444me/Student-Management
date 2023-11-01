from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from account.models import StudentProfile, Teacher
from teacher.models import StudentDetail



# ======================================================
#               Class For Teacher/Student Login 
# ======================================================
class StudentHomePage(TemplateView):
    template_name = 'student/student_home.html'
# ====================== End Class =====================


# ======================================================
#               Class For Teacher/Student Login 
# ======================================================
@method_decorator(login_required, name='dispatch')
class StudentDashbord(TemplateView):
    template_name = 'student/student_dashbord.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        try:
            student_profile = StudentProfile.objects.get(user=user)
            context['student_profile'] = student_profile
        except StudentProfile.DoesNotExist:
            context['student_profile'] = None

        return context
# ====================== End Class =====================

# ======================================================
#               Student Result 
# ======================================================
@login_required 
def student_result(request):
    stu_info = StudentDetail.objects.all()
    return render(request, 'student/student_result.html', {'stu_info': stu_info})
# ====================== End Class =====================

# ======================================================
#               Teacher Contact Info 
# ======================================================
@login_required 
def teacher_info(request):
    teacher_info = Teacher.objects.all()
    return render(request, 'student/teacher_info.html', {'teacher_info': teacher_info})

# ====================== End Class =====================