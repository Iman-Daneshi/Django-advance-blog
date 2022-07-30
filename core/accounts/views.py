from django.views.decorators.cache import cache_page# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from django.core.cache import cache
# import time
from .tasks import sendemail

# Create your views here.


def send_email(request):
    sendemail.delay()
    return HttpResponse("<h1>Done sending</h1>")



# def test(request):
#     if cache.get("test_delay_api") is None:
#         response = requests.get("https://3ea4ba22-59d6-48ff-8d7d-b816da145dd7.mock.pstmn.io/test/delay/5")
#         cache.set("test_delay_api",response.json())
#     return JsonResponse(cache.get("test_delay_api"))


@cache_page(60)
def test(request):
    response = requests.get("https://3ea4ba22-59d6-48ff-8d7d-b816da145dd7.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())
