from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'home.html')
    
def searchTAb(request):
    return render(request,'searchcity.html')

def generateTab(request):
    return render(request,'generate.html')
# Create your views here.
