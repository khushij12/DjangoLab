from django import forms

class loginDetails(forms.Form):
    username = forms.CharField(label="Username: ",max_length=20)
    password = forms.CharField(label="Password",widget = forms.PasswordInput)
