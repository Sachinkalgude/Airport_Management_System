from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import user


class sign_up_form(UserCreationForm):
    password1 = forms.CharField(
        label='password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password*'}))
    password2 = forms.CharField(
        label='confirm password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password*'}))
    Type = forms.ChoiceField(
        choices=(('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs')), initial='Mr', widget=forms.Select(attrs={'class': 'form-control'}))
    nationality = forms.ChoiceField(choices=(('Indian', 'Indian'), ('Foreigners', 'Foreigners')), widget=forms.Select(
        attrs={'class': 'form-control'}), initial='Indian')

    class Meta:
        model = user
        fields = ['email', 'Type', 'first_name', 'Middle_name', 'last_name',
                  'Date_of_birth', 'nationality', 'Where_do_you_live', 'password1', 'password2']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email*', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your Name*', 'class': 'form-control'}),
            'Middle_name': forms.TextInput(attrs={'placeholder': 'Enter your Middle name*', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your Last_name*', 'class': 'form-control'}),
            'Date_of_birth': forms.SelectDateWidget(years=range(1950, 2024), attrs={'class': 'pa'}),
            'Where_do_you_live': forms.TextInput(attrs={'placeholder': 'Enter your Native place*', 'class': 'form-control'}),
        }
