from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


def show_bboard(request):
    return render(request, 'bboard/base_bboard.html')


class BBoardLogin(LoginView):
    template_name = 'bboard/login.html'


@login_required
def profile(request):
    return render(request, 'bboard/profile.html')


class BBoardLogout(LogoutView):
    template_name = 'bboard/logout.html'
