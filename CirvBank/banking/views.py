from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Account, Transaction, TransactionTemplate
from .forms import LoginForm, TransferForm, BanklinkLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from utils import decimalize

def home(request):
    # return render(request, "banking/home.html")
    return render(request, "banking/logout.html")


@login_required
def banklink_template(request):
    account = request.user.account
    # no sesijas templeites id ko izveidoja GET'a
    tt_id = request.session.get("template_id")

    transaction_template = TransactionTemplate.objects.get(pk=tt_id)
    transaction_template.account_from = account

    if request.method == "POST":
        transaction_template.execute()

        # TODO te izlogo useri ara un redirekte kaut kur, kur vajag
        return redirect("bank")
    else:
        context = {"account": account, "template" : transaction_template}
        return render(request, "banking/payment_preview.html", context)


def banklink_login(request):
    form = BanklinkLoginForm()

    if request.method == "POST":
        form = BanklinkLoginForm(request.POST)

        if form.is_valid():
            user = form.login(request)
            if user and user.is_active:
                login(request, user)
                return redirect("banklink_template")
        else:
            form.add_error("", "Nepareizi dati")
            return render(request, 'banking/login_form.html', {'form': form})
    else:
        # TODO varbut vispar GET nevajag lietot, lai var parraidit vairak informacijas
        # no GET parametriem panem infromaciju
        number = request.GET.get("acc")
        sum = request.GET.get("sum")

        # jauns templeit objekts - sitas zinas visu par to ko grib darit lietotajs
        transaction = TransactionTemplate()
        transaction.account_to = Account.from_account_number(number)
        transaction.amount = decimalize(sum)
        transaction.save()

        # TODO tads naivs piegajiens - ar sesiju parsutit (labojam?)
        request.session.__setitem__("template_id", transaction.id)

        return render(request, 'banking/login_form.html', {'form': form})


@login_required
def bank(request):
    account = request.user.account
    context = {"account": account, "transactions": account.transactions(5)}
    return render(request, "banking/overview.html", context)


@login_required
def transactions(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            act_number = form.cleaned_data['account_number']
            amnt = form.cleaned_data['amount']
            sender = request.user.account
            receiver = Account.objects.filter(number=act_number)
            if receiver and amnt > 0 and act_number and receiver[0] != sender:  # Domaju, ka nevajaga
                t = Transaction()  # radit kludu, ja sev suta. Viltnieki
                t.account_to = receiver[0]  # atradusies.
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
    context = {'form': form, "account": account, "transactions": transactions}
    return render(request, 'banking/transactions.html', context)


def user_info(request):
    account = request.user.account
    context = {"account": account}
    return render(request, 'banking/info.html', context)


def user_logout(request):
    logout(request)
    # return render(request, "banking/home.html")
    return render(request, "banking/logout.html")


def user_login(request):  # Labak patik?
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/bank')  # Redirect uz kontrolpanleli
    else:
        form = LoginForm()
        # return render(request, 'banking/login.html', {'form': form})
        return render(request, 'banking/login_new.html', {'form': form})
