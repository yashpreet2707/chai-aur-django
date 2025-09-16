from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello world, you are at chai django home page")
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')


def contact(request):
    return render(request, 'website/contact.html')