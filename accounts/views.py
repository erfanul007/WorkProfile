from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import RegisterForm, CreateUserForm
from .filters import UserFilter

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/dashboard.html')
    # return HttpResponse('Dashboard')


@login_required(login_url='login')
def profile(request, pk_user):
    user = UserInfo.objects.get(username=pk_user)
    context = {'user':user}
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

# def saveFunc(user, email):
#     useri = UserInfo(username=user, email=email)
#     useri.save()
#     userc = UserContact(username=user)
#     userc.save()
#     userd = UserDetails(username=user)
#     userd.save()
#     users = UserSkills(username=user)
#     users.save()
#     usere = UserExperiences(username=user)
#     usere.save()
#     userp = UserProjects(username=user)
#     userp.save()
#     useru = UserAchievements(username=user)
#     useru.save()
#     userg = UserGoal(username=user)
#     userg.save()
#     userpa = UserPassion(username=user)
#     userpa.save()
#     usersc = UserSchool(username=user)
#     usersc.save()
#     userco = UserCollege(username=user)
#     userco.save()
#     userun = UserUniversity(username=user)
#     userun.save()



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                user = form.cleaned_data.get('email')
                # saveFunc(user, email)

                redirect('login')

        context = {'form':form}
        return render(request, 'accounts/register.html', context)


@login_required(login_url='login')
def update(request, pk_user):
    if request.user.username == pk_user:
        user = UserInfo.objects.get(username=pk_user)
        form = RegisterForm(instance=user)
        if request.method == 'POST':
            form = RegisterForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form':form}
        return render(request, 'accounts/update.html', context)
    else:
        return redirect('home')


@login_required(login_url='login')
def searchlist(request):
    user = UserInfo.objects.all()
    # user = order
    myFilter = UserFilter(request.GET, queryset = user)
    user = myFilter.qs

    context = {'user':user,'myFilter':myFilter}

    return render(request, 'accounts/searchlist.html', context)
