from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import UpdateUserForm, CreateUserForm
from .filters import UserFilter

# Create your views here.
@login_required(login_url='login')
def home(request):
    loggedin = request.user.username
    context = {'loggedin': loggedin}
    return render(request, 'accounts/dashboard.html', context)
    # return HttpResponse('Dashboard')


@login_required(login_url='login')
def profile(request, pk_user):
    loggedin = request.user.username
    context = {'loggedin': loggedin}
    user = UserInfo.objects.get(username=pk_user)
    context = {'user':user, 'loggedin':loggedin}
    return render(request, 'accounts/profile.html', context)



def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'incorrect username or password')
        context = {}
        return render(request, 'accounts/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, 'register successfull')
                user = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                # saveFunc(user, email)
                newuser = UserInfo(username=user, email=email)
                newuser.save()

                return redirect('login')


        context = {'form':form}
        return render(request, 'accounts/register.html', context)


@login_required(login_url='login')
def update(request, pk_user):
    loggedin = request.user.username
    if loggedin == pk_user:
        user = UserInfo.objects.get(username=pk_user)
        form = UpdateUserForm(instance=user)
        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance=user)
            form.save()
            messages.info(request, 'update successfull')
            return redirect('home')

        context = {'form':form, 'loggedin': loggedin}
        return render(request, 'accounts/update.html', context)
    else:
        user = UserInfo.objects.get(username=pk_user)
        context = {'user':user, 'loggedin':loggedin}
        messages.info(request, 'Not allowed')
        return redirect('home')


@login_required(login_url='login')
def searchlist(request):
    loggedin = request.user.username
    user = UserInfo.objects.all()
    # user = order
    myFilter = UserFilter(request.GET, queryset = user)
    user = myFilter.qs

    context = {'user':user,'myFilter':myFilter, 'loggedin':loggedin}

    return render(request, 'accounts/searchlist.html', context)
