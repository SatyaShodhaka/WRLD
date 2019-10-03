from django import forms
from django.db import models
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'article',
            'category',
            'image',
        )

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'category',
            'image',
        )