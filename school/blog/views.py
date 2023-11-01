from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm



@login_required
def blog_post(request):
    if request.method == 'POST':
        fm = BlogPostForm(request.POST, label_suffix= ' ')
        if fm.is_valid():
            user = request.user
            if user.is_student:
                fm.instance.user = user
                fm.save()
                return redirect('student_dashbord')
            elif user.is_teacher:
                fm.instance.user = user
                fm.save()
                return redirect('teacher_dashbord') 
    else:
        fm = BlogPostForm(label_suffix= ' ')
    return render(request, 'blog/blog_post.html', {'form': fm})


