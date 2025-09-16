from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello world, you are at chai django home page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello world, you are at chai django about page")


def contact(request):
    return HttpResponse("Hello world, you are at chai django contact page")