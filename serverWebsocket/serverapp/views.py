from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def STest(request):
    return HttpResponse("on serverWebsocket")