from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.forms import  UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from App_Login.forms import SignupForm


# Create your views here.
def is_traffic_(user):
    return user.groups.filter(name='Traffic').exists()


def is_driver_(user):
    return user.groups.filter(name='Driver').exists()


def register_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            grp = Group.objects.get_or_create(name='Driver')
            grp[0].user_set.add(user)
            return HttpResponseRedirect(reverse('App_Login:login'))
    content = {
        'form': form
    }
    return render(request, 'App_Login/register.html', context=content)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('App_main:index'))
        else:
            return render(request, 'App_Login/login.html', {'error': 'username or password is incorrect.'})
    return render(request, 'App_Login/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))

