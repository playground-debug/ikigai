from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.forms import User
from .models import Profile

# Create your views here.


def home(request):
    context = {
        "Profile": Profile.objects.exclude(love__exact='', good__exact='', worldNeed__exact='', paid__exact='')
    }
    return render(request, 'ikigai/home.html', context)


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'ikigai/signup.html')

    else:
        if request.POST['password1'] == request.POST['password2']:

            password = request.POST['password1']
            if len(password) > 4:
                try:
                    user = User.objects.create_user(
                        username=request.POST['username'], password=request.POST['password1'])
                    profile = Profile()
                    profile.user = user
                    user.save()
                    profile.save()
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                except IntegrityError:
                    return render(request, 'ikigai/signup.html', {'error': 'Username already exist'})

            else:
                return render(request, 'ikigai/signup.html', {'error': 'Passwords length must be greater than 4'})

        else:
            return render(request, 'ikigai/signup.html', {'error': 'Passwords does not match'})


@login_required
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'ikigai/login.html')

    else:
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'ikigai/login.html', {'error': 'Invalid Credentials'})

        else:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))


def show(request, profile_id):
    context = {
        "Profile": get_object_or_404(Profile, pk=profile_id)
    }
    return render(request, 'ikigai/show.html', context)


def create(request):
    if request.method == 'GET':
        context = {
            "Profile": Profile.objects.get(user=request.user)
        }
        return render(request, 'ikigai/create.html', context)

    else:
        profile = get_object_or_404(Profile, user=request.user)
        profile.love = request.POST['love']
        profile.good = request.POST['good']
        profile.worldNeed = request.POST['worldNeed']
        profile.paid = request.POST['paid']
        profile.save()
        return HttpResponseRedirect(reverse('home'))
