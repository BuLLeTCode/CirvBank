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
            if receiver:
                t = Transaction()
                t.account_to = receiver[0]
                t.account_from = sender
                t.amount = amnt
                if t.transfer():
                    t.save()
                    return HttpResponseRedirect('/transactions')
                else:
                    form.add_error("amount", "Nepietiek lidzeklu")
            else:
                form.add_error("number", "Nepareizs konta numurs")
    else:
        form = TransferForm()
        account = request.user.account
        context = {'form': form, "account" : account, "transactions": account.transactions()}
    return render(request, 'banking/transactions.html', context)

def user_logout(request):
    logout(request)
    #return render(request, "banking/home.html")
    return render(request, "banking/logout.html")

def user_login(request):
    #TODO sitas viss ir DRAUSMAS, jasalabo lai neizskatas tik briesmigi
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/bank')
                else:
                    pass
                    #nevajadzetu notitk, konts deaktivizets
            else:
                form.add_error("password", "Nepareiza parole vai lietotajvards")
                pass

    else:
        form = LoginForm()

    #return render(request, 'banking/login.html', {'form': form})
	return render(request, 'banking/login_new.html', {'form': form})
