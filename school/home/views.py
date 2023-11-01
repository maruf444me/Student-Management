from django.shortcuts import render
from blog.models import Blog

# ================================================
# Function For Home Page
# ================================================
def home(request):
    post_data = Blog.objects.all().order_by('-id')

    # if request.GET.get('seacrch'):
    #     queryset = Blog.objects.all()
    #     queryset = queryset.filter(title__icontains= request.GET.get('search'))
    return render(request, 'home/home.html', {'post_data': post_data, })
# ================================================

def search_blog(request):
    if request.GET.get('search'):
        query = request.GET.get('search')
        queryset = Blog.objects.filter(title__icontains=query)
    else:
        queryset = Blog.objects.all().order_by('-id')    
    return render(request, 'home/home.html', {'post_data': queryset})