from django import forms
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from home.models import ClassicPoem, Tags
from users.models import User
from django.contrib.auth import authenticate

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat your password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'placeholder': 'Your Name'}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'placeholder': 'Enter Your Password'}),
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data


class AddPost(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)


    class Meta:
        model = ClassicPoem
        fields = [ 'title', 'content', 'tags']

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