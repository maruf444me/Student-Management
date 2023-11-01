from django.contrib import admin
from .models import StudentDetail, TeacherVerify
# For Cusomize admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User, TeacherDetail

# StudentDetail Register 
@admin.register(StudentDetail)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','image','department','roll','city','address','cgpa','grade']
admin.site.register(TeacherVerify)

# # For Customize Admin
# class TeacherDetailInline(admin.StackedInline):
#     model = TeacherDetail
#     can_delete = False

# class CustomUserAdmin(UserAdmin):
#     inlines = (TeacherDetailInline,)

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
