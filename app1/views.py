from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sekhar(request):
    return render(request,'sekhar.html')
def sekhar1(request):
    return HttpResponse('dupe of sekhar')