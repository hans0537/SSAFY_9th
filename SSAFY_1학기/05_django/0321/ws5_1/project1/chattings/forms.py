from django import forms
from .models import Chat

class ChattingForm(forms.ModelForm):
    user = forms.CharField(
        label='작성자',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nickname',
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'rows' : 5,
                'cols' : 50,
                'placeholder':'Chat!',
            }
        )
    )
    class Meta:
        model = Chat
        fields = '__all__'