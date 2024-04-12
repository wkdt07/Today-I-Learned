from .models import Movie,Comment
from django import forms

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'