from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    confirmation_password = forms.CharField(label="Confirm password", widget=forms.PasswordInput())