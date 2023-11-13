from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def karthik(request):
    return render(request,'karthik.html')
def karthik1(request):
    return HttpResponse('dupe of karthik1')