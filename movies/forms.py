from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """form comments"""
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')
