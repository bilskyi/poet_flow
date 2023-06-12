from django import forms
from .models import User


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=255,
        widget=(forms.TextInput(attrs={'value': 'request.username'}))
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'description']

