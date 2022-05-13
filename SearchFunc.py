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
print("Start")

def CityInputDef(citynameInput):
    
    #InputCityName = input()
    
    ApiInputRequest = URL + key + citynameInput + end + apikey + '&units=metric'
    ApiRequest_Input = requests.get(ApiInputRequest)
    data = ApiRequest_Input.json()
    Main = data['main']
    Weather = data['weather']
   
    print(f"Name of the city: {data['name']}")
    print(f"Weather Report: {Weather[0]['description']}")
    print(f"Temperature is: {Main['temp']}")
    print(f"Humidity is: {Main['humidity']}")
   
def generateCities():
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

        print(f"Name of the city: {data['name']}")
        print(f"Weather Report: {Weather[0]['description']}")
        print(f"Temperature is: {Main['temp']}")
        print(f"Humidity is: {Main['humidity']}")
        print(city)
       
       

    print(f"The coldest city is: {cityInfo[CityTemp.index(min(CityTemp))]}")
    AverageTemp = sum(CityTemp) / len(CityTemp)
    print(f"The average Temperature is: {AverageTemp}")
    



