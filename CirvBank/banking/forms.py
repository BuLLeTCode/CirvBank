from django import forms
from django.contrib.auth import authenticate, login, logout

class LoginForm(forms.Form):
    username = forms.CharField(label='Lietotajvards:', max_length=100)
    password = forms.CharField(label='Parole:',widget=forms.PasswordInput())

    def clean(self):#Datu nodzesana
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:#ja tiek veikta konkreti ielogosanas laika, tad iespejams kludas pazinojums
            raise forms.ValidationError("Ielogosanas laika kluda.")
        return self.cleaned_data

    def login(self, request):#Tere naudu! :)
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class TransferForm(forms.Form):
    account_number = forms.CharField(label='Konta numurs', max_length=50)
    amount = forms.DecimalField(label='Summa', max_digits=10, decimal_places=2)


class BanklinkLoginForm(forms.Form):


    username = forms.CharField(label='Lietotajvards:', max_length=100)
    password = forms.CharField(label='Parole:',widget=forms.PasswordInput())
    account_number = forms.CharField(label='Konta numurs', max_length=50)
    amount = forms.DecimalField(label='Summa', max_digits=10, initial=get_initial())

    # TODO
    # TODO
    # TODO
    # TODO sito javar izdarit!!!!! ( vajag iestatit formai sakuma vertibas kaut ka)
    def get_initial(self):
        self.cleaned_data.get("acc")


    def clean(self):#Datu nodzesana
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:#ja tiek veikta konkreti ielogosanas laika, tad iespejams kludas pazinojums
            raise forms.ValidationError("Ielogosanas laika kluda.")
        return self.cleaned_data

    def login(self, request):#Tere naudu! :)
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
