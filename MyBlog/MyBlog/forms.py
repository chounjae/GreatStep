from django import forms
from MyBlog.models import Post

#폼 정의

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title' , 'content']
    