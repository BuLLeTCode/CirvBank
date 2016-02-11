from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Account
from django.template import loader
from django.views import generic
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class DetailView(generic.DetailView):
    model = Account
    template_name = 'accounts/detail.html'

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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
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
                    #nevajadzetu notitk
            else:
                pass
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
