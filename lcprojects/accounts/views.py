from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def accounts(request):
    return HttpResponse("Hello, world. You're at the accounts index.")