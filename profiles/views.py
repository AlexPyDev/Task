from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from .form import LogInForm, CustomUserCreationForm


def user_login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            try:
                user = authenticate(username=form.cleaned_data.get('username'),
                                    password=form.cleaned_data.get('password'))
            except User.DoesNotExist:
                messages.error(request, _("User does not exist."))
                return render(request, 'profiles/login.html', {'form': form})
            if user is not None:
                login(request, user)
                return redirect(request.POST.get('next', 'news:index'))
            # TODO: if not confirmed

    else:
        form = LogInForm()
    return render(request, 'profiles/login.html', {'form': form})


def user_logout(request)  :
    logout(request)
    return redirect('news:index')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            # user.save()
            return render(request, 'news/index.html', {'user_data': user})
    else:
        form = CustomUserCreationForm()
    return render(request, 'profiles/register.html', {'form': form})
