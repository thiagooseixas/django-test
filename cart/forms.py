from django import forms
from .models import Payment


class PostForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('name', 'number_card', 'expiration')
