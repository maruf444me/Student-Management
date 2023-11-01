from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home_page'),
    path('search', search_blog, name='post_search'),
]