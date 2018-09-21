from django.shortcuts import render

# Create your views here.
import json
import hmac
import hashlib
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import hmac
import hashlib

# Using Django
@csrf_exempt
def my_webhook_view(request):
  data = request.body
  signature = request.META['HTTP_X_TAIGA_WEBHOOK_SIGNATURE']
  event = None
  key = 'theverytopsecretkey'
  
  if not verify_signature(key, data, signature):
    return HttpResponse(status=400)

  # Do something with event

  return HttpResponse(status=200)

def verify_signature(key, data, signature):
    mac = hmac.new(key.encode("utf-8"), msg=data, digestmod=hashlib.sha1)
    return mac.hexdigest() == signature
