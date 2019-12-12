from django.shortcuts import render, redirect


def show_main(request):
    return render(request, 'main/base_main.html')
