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

class CityGenerate(object):

    def Generate():
        print("Start")

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
            city_info.append(f"{data['name']} {Weather[0]['description']} {Main['temp']} {Main['humidity']}")
            city_temp.append(Main['temp'])
            print(f"Name of the city: {data['name']}")
            print(f"Weather Report: {Weather[0]['description']}")
            print(f"Temperature is: {Main['temp']}")
            print(f"Humidity is: {Main['humidity']}")
            print(city)

        print(f"The coldest city is: {city_info[city_temp.index(min(city_temp))]}")
        AverageTemp = sum(city_temp) / len(city_temp)
        print(f"The average Temperature is: {AverageTemp}")
        return object()



class InputCity(object):
    def Input():
        input_city_name = input()
        api_input_request = URL + key + input_city_name + end + apikey + '&units=metric'
        api_request = requests.get(api_input_request)
        data = api_request.json()
        main = data['main']
        weather = data['weather']
        print(f"Name of the city: {data['name']}")
        print(f"Weather Report: {weather[0]['description']}")
        print(f"Temperature is: {main['temp']}")
        print(f"Humidity is: {main['humidity']}")


def Execute():
    CityGenerate.Generate()
    InputCity.Input()

Execute()