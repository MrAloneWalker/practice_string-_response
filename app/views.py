from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def giri(request):
    return HttpResponse('<h1>hii bro </h1>')