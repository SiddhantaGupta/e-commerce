from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label="username")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    confirmation_password = forms.CharField(label="Confirm password", widget=forms.PasswordInput())

class ContactForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    address = forms.CharField(label="Address")
    phone_number = forms.CharField(label="Phone Number", widget=forms.TextInput(attrs={'type':'number'}))
    postal_code = forms.CharField(label="zip code", widget=forms.TextInput(attrs={'type':'number'}))