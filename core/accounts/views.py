# from django.shortcuts import render
from django.http import HttpResponse
# import time
from .tasks import sendemail

# Create your views here.


def send_email(request):
    sendemail.delay()
    return HttpResponse("<h1>Done sending</h1>")
