import requests
import json
import random
from tkinter import *
from tkinter import ttk

city = []
city_info =[]
city_temp =[]

apikey="c9a787290254e2833d876e34bbccb790"
URL=f"https://api.openweathermap.org/data/2.5/weather?"
key = "q="
end = "&appid="
class CityGenerate():

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
        




    def Input(input_name):
        
        print("execute?")
        api_input_request = URL + key + input_name + end + apikey + '&units=metric'
        api_request = requests.get(api_input_request)
        data = api_request.json()
        main = data['main']
        weather = data['weather']
        print(f"Name of the city: {data['name']}")
        print(f"Weather Report: {weather[0]['description']}")
        print(f"Temperature is: {main['temp']}")
        print(f"Humidity is: {main['humidity']}")
        return data
        
    
    def tkk_input(city_name , root):
        
        print(city_name)
        c = CityGenerate.Input(city_name)
        print(c)
        cityLabelFind = ttk.Label(root,text=f"city name: {c['name']} weather report: {c['weather'][0]['description']} temperature: {c['main']['temp']} humidity is: {c['main']['humidity']}").place(x=50,y=350)
                

    
    def tkk_output():
        
       
                
        root = Tk()
        root.geometry("400x400"),root.maxsize(800,400),root.minsize(800,400)
        for x in range(5):
            ttk.Label(root,text=f"{city_info[x]}").grid(column=0, row=round(x))
        ttk.Label(root,text=f"The coldest city is: {city_info[city_temp.index(min(city_temp))]}").grid(column=0,row=6)
        average_temp = sum(city_temp) / len(city_temp)
        ttk.Label(root,text=f"The average Temperature is: {average_temp}").grid(column=0,row=7)
        #return
       

        input_field = ttk.Entry(0)
        input_field.place(x=100,y=300) 
        
  
        input_button = ttk.Button(root,command=lambda :CityGenerate.tkk_input(input_field.get(),root),text ="Search city").place(x=5,y=300)
        
        root.mainloop()
    

def Execute():
    CityGenerate.Generate()
    CityGenerate.tkk_output()


Execute()