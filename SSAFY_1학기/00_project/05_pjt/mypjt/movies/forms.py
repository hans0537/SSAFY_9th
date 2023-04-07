from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
    score = forms.FloatField(widget=forms.NumberInput(attrs={'step':0.5, 'min':0.5, 'max':5.0}))
    release_date = forms.DateField(widget=forms.NumberInput(attrs={'type' : 'date'}))