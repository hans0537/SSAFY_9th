from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('user', 'like_users',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('movie', 'user', 'parent_comment')
