from django import forms
from .models import Blog


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['user', 'created']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'},),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Post Title',
            'content': 'Post Content',
        }