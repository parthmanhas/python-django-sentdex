from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content':['Hello There!','If you want to contact me, contact me at','parthmanhas@gmail.com']})
