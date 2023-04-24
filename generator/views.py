from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, "generator/home.html")

def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    
    
    length = int(request.GET.get("length", 12))
    special = request.GET.get("specail")
    uppercase = request.GET.get("uppercase")
    numbers = request.GET.get("numbers")
    
    
    if numbers:
        chars += list('0123456789')
    
    if uppercase:
        chars += list('abcdefghijklmnopqrstuvwxyz'.upper())

    if special:
        chars += list('!@#$%^&*()_+|"}{?><')

    password = ""
    for i in range(length):
        password += random.choice(chars)
    
    return render(request, "generator/password.html", {"password": password})


def about(request):
    return render(request, "generator/about.html")
