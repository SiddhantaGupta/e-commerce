from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label="username", widget=forms.TextInput(
        attrs={
        'class':'form-control my-2',
        }
    ))
    email = forms.EmailField(label="Email", widget=forms.TextInput(
        attrs={
        'class':'form-control my-2',
        }
    ))
    password = forms.CharField(label="Password", widget=forms.TextInput(
        attrs={
        'type': 'password',
        'class':'form-control my-2',
        }
    ))
    confirmation_password = forms.CharField(label="Confirm password", widget=forms.TextInput(
        attrs={
        'type': 'password',
        'class':'form-control my-2',
        }
    ))

class ContactForm(forms.Form):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(
        attrs={
        'class':'form-control my-2',
        }
    ))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(
        attrs={
        'class':'form-control my-2',
        }
    ))
    address = forms.CharField(label="Address", widget=forms.TextInput(
        attrs={
        'class':'form-control my-2',
        }
    ))
    phone_number = forms.IntegerField(label="Phone Number", widget=forms.TextInput(
        attrs={
        'class':'form-control my-2',
        }
    ))
    postal_code = forms.IntegerField(label="zip code", widget=forms.TextInput(
        attrs={
        'class':'form-control my-2',
        }
    ))