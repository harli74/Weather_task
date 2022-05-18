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
dataLenht =''
cities_db_info=[]
inputCount =0


def refreshcounter(request):
    dataLenht = Cities.objects.count()

# Create your views here.
def main_def(request):
    
    print('fafsafas')
   # test_print = Cities.objects.get(id=1)
   # print(test_print)
    return render(request, 'home.html')

def searchTab(request):
   
    dataLenht = Cities.objects.count()
    print(cities_db_info)
    dataLenht = Cities.objects.count()
    nameData = request.POST.get('Search')
    print(nameData)
    btnRefresh = request.GET.get('btnRefresh')
    btnDelete=request.POST.get('btnDelete')
    
    #print(Cities.objects.get(id=206))
    
    
    
    if nameData != None:
        ApiInputRequest = f"{URL}{key}{nameData}{end}{apikey}&units=metric"
        ApiRequest_Input = requests.get(ApiInputRequest)
        dataweather = ApiRequest_Input.json()
        Main = dataweather['main']
        Weather = dataweather['weather']
        dataLenht = Cities.objects.count()
        
        for x in range(Cities.objects.count()): 
            shanolud = Cities.objects.get(id=x)
            refreshcounter(request)
        if Cities.objects.all().count()<10:
            Cities.objects.create(id = Cities.objects.count(),city_name=nameData,humidity=Main['humidity'],temperature=Main['temp'],weather =Weather[0]['description'])
            
            print(Cities.objects.count())
            dataLenht = Cities.objects.count()
            
            
            #print(shanolud.city_name,shanolud.weather,shanolud.temperature,shanolud.humidity)
            dataLenht =0
            cities_db_info.clear()
            for x in range(Cities.objects.count()):
                shanolud= Cities.objects.get(id=x)
                cities_db_info.append(f"{shanolud.city_name} {shanolud.temperature} {shanolud.humidity} {shanolud.weather}")
                #append(f"{data['name']} {Weather[0]['description']} {Main['temp']} {Main['humidity']}")
                dataLenht=+1
        elif Cities.objects.all().count()>10:
            print("gg")

    print(dataLenht)
    refreshcounter(request)

            
        #Cities.objects.get(id=0).delete()
    if btnDelete != None:
        print("deleting")
        Cities.objects.all().delete()
        dataLenht = Cities.objects.count()
    if(btnRefresh != None):

        print("refresh")
        refreshcounter(request)
        dataLenht = Cities.objects.count()
        
    print("Do something")
    #delete all values of the table
    #
    #Cities.refresh_from_db(self=Cities)
    #Cities.save()
   # Cities.refresh_from_db()
    
    return render(request,'searchcity.html',{'input_data':nameData,'db_lenght':dataLenht,'city_info':cities_db_info})