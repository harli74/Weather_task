import requests
import random 
import time
import json

apilinksfromid=[]
randcodes=[]
def locationcodes():
    with open('city.list.json',encoding='UTF-8') as json_file:
        data = json.load(json_file)
        for i in data:
            randcodes.append(i['id'])

    #for i in range(random.randint(0,len(randcodes))): #not using this for the sake of fast runtime
    for i in range(random.randint(20,40)):
        complete_api_link="https://api.openweathermap.org/data/2.5/weather?id="+ str(randcodes[i])+"&appid=eb26abb859972dffb7a0c0001421729b&units=metric"
        api_link=requests.get(complete_api_link)
        time.sleep(0.32)
        api_data=api_link.json()
        apilinksfromid.append(api_data) 
    #print (apilinksfromid)

def average():
         tempsum=0.0
         avg=0.0
         numberoftowns=len(apilinksfromid)
  
         for i in range(numberoftowns):

             town_temps=(apilinksfromid[i]['main']['temp'])
             tempsum+=town_temps

         return numberoftowns,tempsum/numberoftowns

def coldest():
    mintemp=9000
    coldesttown=" "
    for i in range(len(apilinksfromid)):
        town_temps=(apilinksfromid[i]['main']['temp'])
        if apilinksfromid[i]['main']['temp']<mintemp:
           mintemp=apilinksfromid[i]['main']['temp']

    for i in range(len(apilinksfromid)):
        if mintemp==apilinksfromid[i]['main']['temp']:
            coldesttown=apilinksfromid[i]['name']

    return coldesttown
 
def singletowncheck(input):
    location=input
    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=eb26abb859972dffb7a0c0001421729b&units=metric"
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()
    if api_data['cod']=='404':
        print("Wrong city{}",format(location))
    else:
        town_temps=(api_data['main']['temp']) 
        weather=(api_data['weather'][0]['description'])
        hmdt=api_data['main']['humidity']
        return town_temps,weather,hmdt
