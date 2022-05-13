from cgitb import text
from curses import BUTTON1_PRESSED
from logging import root
from multiprocessing.sharedctypes import Value
from numbers import Number
from operator import index, indexOf, truediv
import string
from tokenize import Double
from turtle import left, position


from unicodedata import name
from click import command
import requests
import json
import random
from tkinter import *
from tkinter import ttk



#buttonGenerator = ttk.Button(root,command=generateCities,text="Generate 5 Random Cities").place(x=5,y=50)

# ttk.Label(root, text="City1").grid(column=20, row=0)
# ttk.Label(root, text="City2").grid(column=20, row=1)
# ttk.Label(root, text="City3").grid(column=20, row=2)
# ttk.Label(root, text="City4").grid(column=20, row=3)
# ttk.Label(root, text="City5").grid(column=20, row=4)

#ttk.Entry(frm, text="City5").grid(column=20, row=4),Place("200x200")

#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=40, row=40)


city = []
cityInfo =[]
CityTemp =[]
frm = 0
apikey="c9a787290254e2833d876e34bbccb790"
URL=f"https://api.openweathermap.org/data/2.5/weather?"
key = "q="
end = "&appid="
print("Start")
def clear_widget_text(widget):
    widget['text'] = ""


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
       
        ttk.Label(root,text=f"City name: {data['name']} Weather is: {Weather[0]['description']} Temperature: {Main['temp']} Humidity: {Main['humidity']}").grid(column=0, row=round(x))

    print(f"The coldest city is: {cityInfo[CityTemp.index(min(CityTemp))]}")
    AverageTemp = sum(CityTemp) / len(CityTemp)
    print(f"The average Temperature is: {AverageTemp}")
    ttk.Label(root,text=f"The coldest city is: {cityInfo[CityTemp.index(min(CityTemp))]}").grid(column=0,row=6)
    ttk.Label(root,text=f"The average Temperature is: {AverageTemp}").grid(column=0,row=7)

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
    cityLabelFind = ttk.Label(root,text=f"City name: {data['name']} Weather is: {Weather[0]['description']} Temperature: {Main['temp']} Humidity: {Main['humidity']}").place(x=50,y=350)
    clear_widget_text(InputField.delete())
    
root = Tk()
root.geometry("400x400"),root.maxsize(800,400),root.minsize(800,400)

def btnClick():
    CityInputDef(InputField.get())
    

buttonGenerator = ttk.Button(root,command=generateCities,text="Generate 5 Random Cities").place(x=5,y=150)
InputField = ttk.Entry(frm, text=f"Burgas")
InputField.place(x=100,y=300)
InputButton = ttk.Button(root,command=btnClick,text ="Search city").place(x=5,y=300)

root.mainloop()