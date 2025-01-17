from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['review', 'user', 'parent_comment']
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': 1, 'cols': 5, 'class': 'col-2'},
            ),
        }