from django.http import HttpResponse
from django.shortcuts import render

def index(request) :
    return render(request , "index.html")

def diary(request) :
    return render(request , "diary.html")