from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
# Create your views here.
from catalog.forms import SignUpForm






from django.http import HttpResponseRedirect
from django.shortcuts import render



def first(req):
    return render(req, 'index.html')
def index(req):
    return render(req, 'index.html')

def profile(request):
    args = {'user':request.user}
    return render(request, 'profile.html', args)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/test')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def test(request):
    return render(request, 'test.html')
    


def welcome(request):
    return render(request, 'test.html')

