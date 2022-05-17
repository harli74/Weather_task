from ast import Delete
from django.shortcuts import render 
import requests
from .models import Cities





# Create your views here.
def main_def(request):
    
    print('fafsafas')
    return render(request, 'home.html')

def searchTab(request):
    #Cities.objects.create(city_name='Burgas',humidity=5,temperature=18,weather ='rain')
    #delete all values of the table
    Cities.objects.all().delete()
            
    
    return render(request,'searchcity.html')