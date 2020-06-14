from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user',
               'id': 'exampleInputUsername',
               'placeholder': 'Username'}))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-user',
               'id': 'exampleInputPassword',
               'placeholder': 'Password'}))
