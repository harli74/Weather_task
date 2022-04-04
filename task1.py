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
         return avg       
def  coldest():
     mintemp=9000
     coldesttown=" "
     for i in range(len(apilinksfromid)):
         api_data=apilinksfromid[i].json()
         town_temps=((api_data['main']['temp'])-273.15)
         if town_temps<mintemp:mintemp=town_temps
         if mintemp==town_temps:coldesttown=api_data['name']
     return coldesttown  
def singletowncheck(input):
    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+input+"&appid=f24acb33b0bcc507760fec5abaa0313a"
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()
    if api_data['cod']=='404':
        print("Wrong city{}",format(location))
    else:
        town_temps=((api_data['main']['temp'])-273.15) 
        weather=(api_data['weather'][0]['description'])
        hmdt=api_data['main']['humidity']
        return town_temps,weather,hmdt
        
        
#singletowncheck()
#def averagetogui():

def singletownsearch():
    temps,weather,hmdt=singletowncheck(modify.get())
    outputtemp.set("Stats of "+modify.get()+" are :\n Temps:"+str(temps)+"\n Weather: "
                   +weather+"\n Humidity: "+str(hmdt)+" %")
    
appwindow=Tk()
root=appwindow
outputtemp=StringVar()
outputavg=StringVar()
appwindow.title("City Checker App")
appwindow.geometry('640x480')
lblsearch=Label(appwindow,text='Enter City to Find:').grid(column=0,row=1)
lblsearch=Label(appwindow,textvariable=outputtemp).grid(column=0,row=2)
modify=Entry(root)
modify.grid(column=1, row=1)
btn3=Button(appwindow,text="Check City:",fg="black",command=singletownsearch).grid(column=2,row=1)
lblrand_cities = Label(appwindow, text="Random Cities:").grid(column=0, row=0)
btn = Button(appwindow, text="Collect Data!",fg="red",command=locationcodes).grid(column=1, row=0)
lblaveragevalue = Label(appwindow, text="Random Cities:").grid(column=0, row=3)
lblaverageguiresponce=Label(appwindow,textvariable=outputavg).grid(column=2,row=3)
btn1=Button(appwindow,text="AverageTemps",command=average).grid(column=1,row=3)
#btn2=Button(appwindow,text="Coldest City:",fg="blue",command=coldest).grid(column=3,row=0)
btn4=ttk.Button(appwindow, text="Quit", command=root.destroy).grid(column=5, row=5)
root.mainloop()
appwindow.mainloop()