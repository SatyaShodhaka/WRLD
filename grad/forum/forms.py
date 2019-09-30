from django import forms
from django.db import models
from .models import Post
class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'category',
            'image',
        ]
        def save(self, commit = True):
            Post.title = self.cleaned_data['title']
            Post.description = self.cleaned_data['description']
            Post.category = self.cleaned_data['category']
            Post.image = self.cleaned_data['image']
            if commit:
                Post.save()
            return Post