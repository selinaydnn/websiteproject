from django import forms

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
