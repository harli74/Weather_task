from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
import requests
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
savedData =[]


def home(request):
    return render(request,'home.html')



def searchTAb(request):
    nameData = request.POST.get('Search')
    savedData.clear()
    savedData.append(nameData)
    print(nameData)
    ApiInputRequest = f"{URL}{key}{nameData}{end}{apikey}&units=metric"
    ApiRequest_Input = requests.get(ApiInputRequest)
    dataweather = ApiRequest_Input.json()
    Main = dataweather['main']
    Weather = dataweather['weather']

   
    return render(request,'searchcity.html',{'inputData':nameData,'weather':Weather[0]['description'],'dataTemp':Main['temp'],'humidity':Main['humidity']})
    
def generateTab(request):
    city.clear()
    cityInfo.clear()
    CityTemp.clear()
    with open('Resources/city.list.json','r') as f:
     cityData = json.load(f)
    Allcount =0
    for x in range(0,len(cityData)):
     Allcount+=1

    print(Allcount)

    for x in range(5):
        randomNumber = random.randrange(0,Allcount)
        city.append(cityData[randomNumber]['name'])

        apiRequest = URL + key + city[x] + end + apikey + '&units=metric'
        ApiOutput = requests.get(apiRequest)
        data = ApiOutput.json()
        Main = data['main']
        Weather = data['weather']

        cityInfo.append(f"{data['name']} {Weather[0]['description']} {Main['temp']} {Main['humidity']}")
        CityTemp.append(Main['temp'])
    
        coldestCityOutput=f"The coldest city is: {cityInfo[CityTemp.index(min(CityTemp))]}"
        AverageTemp = f"The average temperature is: {sum(CityTemp) / len(CityTemp)}"
    return render(request,'generate.html',{'temp':CityTemp,'cityName':cityInfo,'coldestCity':cityInfo[CityTemp.index(min(CityTemp))],'averageTemp':(sum(CityTemp) / len(CityTemp))})


# Create your views here.
