from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import datetime
def index(request):
    return HttpResponse("Hello World!!")

def formHttpText(request):
    return HttpResponse("<h1>Hello World</h1>")

def dateTime(request):
    return HttpResponse(datetime.datetime.now())