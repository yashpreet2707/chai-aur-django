from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello world, you are at chai django home page")

def about(request):
    return HttpResponse("Hello world, you are at chai django about page")


def contact(request):
    return HttpResponse("Hello world, you are at chai django contact page")