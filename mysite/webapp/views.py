from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h2>Hey There Boy!</h2>") 
