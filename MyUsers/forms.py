from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from base.models import Reader


class RegisterForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.DateInput())

    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'bio']


class EditForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = [ 'bio',]


class LoginForm(AuthenticationForm):
    class Meta:
        model = Reader
        fields = '__all__'
