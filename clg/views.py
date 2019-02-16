from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'clg/home.html')

def about(request):
    return render(request, 'clg/about.html')


def admission(request):
    return render(request, 'clg/admission.html')

def contact(request):
    return render(request, 'clg/contact.html')