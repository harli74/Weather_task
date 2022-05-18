from django.shortcuts import render
import requests
from .models import Cities
import json
import random
city = []
cityInfo =[]
CityTemp =[]
Weather=''
frm = 0
apikey="c9a787290254e2833d876e34bbccb790"
URL=f"https://api.openweathermap.org/data/2.5/weather?"
key = "q="
end = "&appid="




# Create your views here.
def main_def(request):
    
    print('fafsafas')
   # test_print = Cities.objects.get(id=1)
   # print(test_print)
    return render(request, 'home.html')

def searchTab(request):
    dataLenht = Cities.objects.count()
    nameData = request.POST.get('Search')
    print(nameData)

    btnDelete=request.POST.get('btnDelete')
    
    #print(Cities.objects.get(id=206))
    
    
    # for x in range(10): 
    #    Cities.objects.create(city_name='Burgas',humidity=5,temperature=18,weather ='rain')
    # print(Cities.objects.all().count())
    if nameData != None:
        ApiInputRequest = f"{URL}{key}{nameData}{end}{apikey}&units=metric"
        ApiRequest_Input = requests.get(ApiInputRequest)
        dataweather = ApiRequest_Input.json()
        Main = dataweather['main']
        Weather = dataweather['weather']
        if Cities.objects.all().count()<10:
            Cities.objects.create(city_name=nameData,humidity=Main['humidity'],temperature=Main['temp'],weather =Weather[0]['description'])
            print(Cities.objects.count())
            
        #Cities.objects.get(id=0).delete()
    if btnDelete != None:
        print("deleting")
        Cities.objects.all().delete()
    print("Do something")
    #delete all values of the table
    #
    #Cities.refresh_from_db(self=Cities)
    #Cities.save()
   # Cities.refresh_from_db()
    
    return render(request,'searchcity.html',{'input_data':nameData,'db_lenght':dataLenht,})