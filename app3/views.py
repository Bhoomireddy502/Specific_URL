from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def raja(request):
    return render(request,'raja.html')
def raja1(request):
    return HttpResponse('dupe of raja1')