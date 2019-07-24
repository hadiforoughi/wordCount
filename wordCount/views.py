from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html',{'hi':'hes'})
	
def count (request):
	text=request.GET['fulltext']
	return render (request,'count.html',{'text':text})

def info (request):
	return render (request,'info.html')
