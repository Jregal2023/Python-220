#forms are cool in django.. because we use a modelw e can just grab the things we want from our model to display as
#text boxes or inputs
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)