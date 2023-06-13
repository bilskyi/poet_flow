from django import forms
from .models import User

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)
    description = forms.CharField(
        required=False,
        widget=forms.Textarea()
    )
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'description', 'avatar']