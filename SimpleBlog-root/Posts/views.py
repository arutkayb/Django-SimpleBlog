from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello(request):
	now = datetime.datetime.now()
	return HttpResponse(str(now))
