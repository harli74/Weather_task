import requests
import random 
import time
apilinksfromid=[]
randcodes=[]
rnd=random.randint(20,100)
def locationcodes():
    randcodes=random.sample(range(833, 102908597), 1000) 
    for i in range(len(randcodes)):
        complete_api_link="https://api.openweathermap.org/data/2.5/weather?id="+str(randcodes[i])+"&appid=eb26abb859972dffb7a0c0001421729b"
        api_link=requests.get(complete_api_link)
        if api_link.ok:
            api_data=api_link.json()
            if api_data['cod']!=['404']:
                apilinksfromid.append(api_data)
        else: 
            time.sleep(0.3)
   
    print (apilinksfromid)

def average():
         tempsum=0.0
         avg=0.0
         numberoftowns=rnd
  
         for i in range(numberoftowns): 
             api_data=apilinksfromid[i].json()
             town_temps=((api_data['main']['temp'])-273.15)
             tempsum+=town_temps
             avg=tempsum/numberoftowns 
             
         return numberoftowns,avg

def  coldest():
     mintemp=9000
     coldesttown=" "
     for i in range(len(apilinksfromid)):
         api_data=apilinksfromid[i].json()
         town_temps=((api_data['main']['temp'])-273.15)
         if town_temps<mintemp:
             mintemp=town_temps
         if mintemp==town_temps:
             coldesttown=api_data['name']
     return coldesttown
 
def singletowncheck(input):
    location=input
    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=eb26abb859972dffb7a0c0001421729b"
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()
    if api_data['cod']=='404':
        print("Wrong city{}",format(location))
    else:
        town_temps=((api_data['main']['temp'])-273.15) 
        weather=(api_data['weather'][0]['description'])
        hmdt=api_data['main']['humidity']
        return town_temps,weather,hmdt
