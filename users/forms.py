from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label="username")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    confirmation_password = forms.CharField(label="Confirm password", widget=forms.PasswordInput())