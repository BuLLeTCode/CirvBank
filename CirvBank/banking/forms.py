from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Lietotajvards:', max_length=100)
    password = forms.CharField(label='Parole:',widget=forms.PasswordInput())

class TransferForm(forms.Form):
    account_number = forms.CharField(label='Konta numurs', max_length=50)
    amount = forms.DecimalField(label='Summa', max_digits=10, decimal_places=2)
