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
            city_data = json.load(f)


        all_count =0
        for x in range(0,len(city_data)):
            all_count+=1

        print(all_count)

        for x in range(5):
            random_number = random.randrange(0,all_count)
            city.append(city_data[random_number]['name'])

            
            api_request = URL + key + city[x] + end + apikey + '&units=metric'
            api_output = requests.get(api_request)

            data = api_output.json()
            main = data['main']
            weather = data['weather']
            city_info.append(f"{data['name']} {weather[0]['description']} {main['temp']} {main['humidity']}")
            city_temp.append(main['temp'])
            print(f"Name of the city: {data['name']}")
            print(f"Weather Report: {weather[0]['description']}")
            print(f"Temperature is: {main['temp']}")
            print(f"Humidity is: {main['humidity']}")
            print(city)

        print(f"The coldest city is: {city_info[city_temp.index(min(city_temp))]}")
        average_temp = sum(city_temp) / len(city_temp)
        print(f"The average Temperature is: {average_temp}")
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