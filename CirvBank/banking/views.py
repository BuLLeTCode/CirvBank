from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Account, Transaction
from django.template import loader
from django.views import generic
from .forms import LoginForm, TransferForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    #return render(request, "banking/home.html")
	return render(request, "banking/logout.html")


@login_required
def bank(request):
    account = request.user.account
    context = {"account" : account, "transactions": account.transactions(5)}
    return render(request, "banking/overview.html", context)

@login_required
def transactions(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            act_number = form.cleaned_data['account_number']
            amnt= form.cleaned_data['amount']
            sender = request.user.account
            receiver = Account.objects.filter(number = act_number)
            if receiver and amnt > 0 and act_number and receiver[0] != sender:#Domaju, ka nevajaga
                t = Transaction()                                             #radit kludu, ja sev suta. Viltnieki
                t.account_to = receiver[0]                                    #atradusies.
                t.account_from = sender
                t.amount = amnt
                if t.transfer():
                    t.save()
                    return HttpResponseRedirect('/transactions')
                else:
                    form.add_error("amount", "Nepietiek lidzeklu")
            else:
                form.add_error("", "Nepareizi dati")
    else:
        form = TransferForm()

    account = request.user.account
    transactions = account.transactions()
    context = {'form': form, "account" : account, "transactions": transactions}
    return render(request, 'banking/transactions.html', context)

def user_info(request):
    account = request.user.account
    context = {"account" : account}
    return render(request, 'banking/info.html', context)

def user_logout(request):
    logout(request)
    #return render(request, "banking/home.html")
    return render(request, "banking/logout.html")

def user_login(request):#Labak patik?
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/bank')# Redirect uz kontrolpanleli
    else:
        form = LoginForm()
    #return render(request, 'banking/login.html', {'form': form})
	return render(request, 'banking/login_new.html', {'form': form})
