import weakref
from django.shortcuts import render
import requests
from .models import Cities
import json
import random

city = []
city_info =[]
city_temp =[]
apikey="c9a787290254e2833d876e34bbccb790"
URL=f"https://api.openweathermap.org/data/2.5/weather?"
key = "q="
end = "&appid="
data_lenght =''
cities_db_info=[]
input_count =0
city_object=''
field_1=0
field_2=0
def refreshcounter(request):
    data_lenght = Cities.objects.count()

# Create your views here.
def main_def(request):
    
    print('fafsafas')
   # test_print = Cities.objects.get(id=1)
   # print(test_print)
    return render(request, 'home.html')





def searchTab(request):
 
    compare_btn = request.POST.get('compare')
    field_1 = request.POST.get('id_1')
    field_2 = request.POST.get('id_2')
    data_lenght = Cities.objects.count()
    print(cities_db_info)
    data_lenght = Cities.objects.count()
    name_data = request.POST.get('Search')
    print(name_data)
    btn_refresh = request.POST.get('btnRefresh')
    btn_delete=request.POST.get('btnDelete')
    
    #print(Cities.objects.get(id=206))
    
    
    
    if name_data != None:
        api_input_request = f"{URL}{key}{name_data}{end}{apikey}&units=metric"
        api_request_input = requests.get(api_input_request)
        data_weather = api_request_input.json()
        main = data_weather['main']
        weather = data_weather['weather']
        data_lenght = Cities.objects.count()
        
        for x in range(Cities.objects.count()): 
            city_object = Cities.objects.get(id=x)
            refreshcounter(request)
        if Cities.objects.all().count()<10:
            Cities.objects.create(id = Cities.objects.count(),city_name=name_data,humidity=main['humidity'],temperature=main['temp'],weather =main[0]['description'])
            
            print(Cities.objects.count())
            data_lenght = Cities.objects.count()
            
            
            #print(city_object.city_name,city_object.weather,city_object.temperature,city_object.humidity)
            data_lenght =0
            
            for x in range(Cities.objects.count()):
                city_object= Cities.objects.get(id=x)
               
                #append(f"{data['name']} {Weather[0]['description']} {Main['temp']} {Main['humidity']}")
                data_lenght=+1
        elif Cities.objects.all().count()>10:
            print("gg")

    print(data_lenght)
    refreshcounter(request)

            
        #Cities.objects.get(id=0).delete()
    if btn_delete != None:
        print("deleting")
        Cities.objects.all().delete()
        data_lenght = Cities.objects.count()
    if(btn_refresh != None):
        
        print("refresh")
        refreshcounter(request)
        Cities.objects.all().order_by('temperature')
        data_lenght = Cities.objects.count()
        cities_db_info.clear()
        for x in range(Cities.objects.count()):
                city_object= Cities.objects.get(id=x)
                cities_db_info.append(f"{city_object.city_name} {city_object.temperature} {city_object.humidity} {city_object.weather}")
                #append(f"{data['name']} {Weather[0]['description']} {Main['temp']} {Main['humidity']}")
                data_lenght=+1
        
        
        return render(request,'searchcity.html',{'input_data':name_data,'db_lenght':data_lenght,'city_info':cities_db_info})
        
    if compare_btn != None:
        if field_1 != None and field_2 != None:
           
            print("compare")
          
            city_object1=Cities.objects.get(id=field_1)
            city_object2=Cities.objects.get(id=field_2)
            city_1_info = f"{city_object1.city_name} {city_object1.temperature} {city_object1.humidity} {city_object1.weather}"
            city_2_info = f"{city_object2.city_name} {city_object2.temperature} {city_object2.humidity} {city_object2.weather}"
          
            return render(request,'searchcity.html',{'field1':city_1_info,'field2':city_2_info,})
    print("Do something")
    #delete all values of the table
    #
    #Cities.refresh_from_db(self=Cities)
    #Cities.save()
   # Cities.refresh_from_db()
   
    print(field_1)
    print(field_2)
    return render(request,'searchcity.html',{'input_data':name_data,'db_lenght':data_lenght,'city_info':cities_db_info,})