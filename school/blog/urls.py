from django.urls import path
from .views import *


urlpatterns = [
    path('', blog_post, name='blog'),
]