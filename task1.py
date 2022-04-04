import requests
import random
from tkinter import *
from tkinter import ttk
randcodes=[]
apilinksfromid=[]

def locationcodes():
    global randcodes
    global apilinksfromid
    rnd=random.randint(20,100)
    for i in range(1000):
        randcodes.append(random.randint(833,102908597))
    for i in range(rnd):
        complete_api_link="https://api.openweathermap.org/data/2.5/weather?id="+str(randcodes[i])+"&appid=f24acb33b0bcc507760fec5abaa0313a"
        api_link=requests.get(complete_api_link)
        api_data=api_link.json()
        if api_data['cod']!='404':
            apilinksfromid.append(api_link)
def average():
         sum=0
         avg=0
         for i in range(len(apilinksfromid)): 
             api_data=apilinksfromid[i].json()
             town_temps=((api_data['main']['temp'])-273.15)
             sum+=town_temps
             avg=sum/5
         print ("Average temperature is ",avg)         
def  coldest():
     mintemp=9000
     coldesttown=" "
     for i in range(len(apilinksfromid)):
         api_data=apilinksfromid[i].json()
         town_temps=((api_data['main']['temp'])-273.15)
         if town_temps<mintemp:mintemp=town_temps
         if mintemp==town_temps:coldesttown=api_data['name']
     print("Coldest town is:",coldesttown)  
def singletowncheck(input):
    #location=input()
    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+input+"&appid=f24acb33b0bcc507760fec5abaa0313a"
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()
    if api_data['cod']=='404':
        print("Wrong city{}",format(location))
    else:
        town_temps=((api_data['main']['temp'])-273.15) 
        weather=(api_data['weather'][0]['description'])
        hmdt=api_data['main']['humidity']
        print("Temp: {}".format(town_temps))
        print("Weather Description: ",weather)
        print("Humidity: ",hmdt,'%')
#singletowncheck()
def singletownsearch():
    print("Stats of "+modify.get()+" are :")
    singletowncheck(modify.get())
appwindow=Tk()
root=appwindow
appwindow.title("City Checker App")
appwindow.geometry('640x480')
lblsearch=Label(appwindow,text='Enter City to Find:')
lblsearch.grid(column=0,row=1)
modify=Entry(root)
modify.grid(column=1, row=1)
modify.focus_set()
lblrand_cities = Label(appwindow, text="Random Cities:")
lblrand_cities.grid(column=0, row=0)
btn = Button(appwindow, text="Collect Data!",fg="red",command=locationcodes)
btn.grid(column=1, row=0)
btn1=Button(appwindow,text="AverageTemps",command=average)
btn1.grid(column=2,row=0)
btn2=Button(appwindow,text="Coldest City:",fg="blue",command=coldest)
btn2.grid(column=3,row=0)
btn3=Button(appwindow,text="Check City:",fg="black",command=singletownsearch)
btn3.grid(column=2,row=1)
btn4=ttk.Button(appwindow, text="Quit", command=root.destroy).grid(column=1, row=5)
root.mainloop()
appwindow.mainloop()

