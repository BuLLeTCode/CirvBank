from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Account
from django.template import loader
from django.views import generic
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")

@login_required
def bank(request):
    account = request.user.account
    context = {"account" : account}
    return render(request, "accounts/overview.html", context)

def user_logout(request):
    logout(request)
    return render(request, "home.html")

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
                pass

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
