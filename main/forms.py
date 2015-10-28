from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from main.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ['email']
        exclude = ['username']


class UserSignUp(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class UserLogin(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    
