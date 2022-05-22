from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
import random
city = []
city_info =[]
city_temp =[]
apikey="c9a787290254e2833d876e34bbccb790"
URL=f"https://api.openweathermap.org/data/2.5/weather?"
key = "q="
end = "&appid="
saved_data =[]


def home(request):
    return render(request,'home.html')



def searchTAb(request):
    name_data = request.POST.get('Search')
    saved_data.clear()
    saved_data.append(name_data)
    print(name_data)
    api_input_request = f"{URL}{key}{name_data}{end}{apikey}&units=metric"
    api_request_input = requests.get(api_input_request)
    data_weather = api_request_input.json()
    main = data_weather['main']
    weather = data_weather['weather']

   
    return render(request,'searchcity.html',{'input_data':name_data,'weather':weather[0]['description'],'data_temp':main['temp'],'humidity':main['humidity']})
    
def generateTab(request):
    city.clear()
    city_info.clear()
    city_temp.clear()
    with open('Resources/city.list.json','r') as f:
     city_data = json.load(f)
    all_count =0
    for x in range(0,len(city_data)):
     all_count+=1

    print(all_count)

    for x in range(5):
        randomNumber = random.randrange(0,all_count)
        city.append(city_data[randomNumber]['name'])

        apiRequest = URL + key + city[x] + end + apikey + '&units=metric'
        ApiOutput = requests.get(apiRequest)
        data = ApiOutput.json()
        Main = data['main']
        Weather = data['weather']

        city_info.append(f"{data['name']} {Weather[0]['description']} {Main['temp']} {Main['humidity']}")
        city_temp.append(Main['temp'])
    
        coldest_city_output=f"The coldest city is: {city_info[city_temp.index(min(city_temp))]}"
        average_temp = f"The average temperature is: {sum(city_temp) / len(city_temp)}"
    return render(request,'generate.html',{'temp':city_temp,'city_name':city_info,'coldest_city':city_info[city_temp.index(min(city_temp))],'average_temp':(sum(city_temp) / len(city_temp))})


# Create your views here.
