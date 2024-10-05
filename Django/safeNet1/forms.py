# myapp/forms.py
from django import forms

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    surname = forms.CharField(max_length=30, required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget())
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], required=True)
    mobile_number = forms.CharField(max_length=15, required=True)
    confirm_contact = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    confirm_email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)
