import requests
strs=[]
apilinks=[]
def locationlist():
  for i in range(5):
      strs.append(input())
locationlist()

def createapilinks():
 for i in range(5):
   complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+strs[i]+"&appid=f24acb33b0bcc507760fec5abaa0313a"
   api_link=requests.get(complete_api_link)
   apilinks.append(api_link)
createapilinks()
#print (apilinks)
def average():
    sum=0
    avg=0
    for i in range(5): 
        api_data=apilinks[i].json()
        town_temps=((api_data['main']['temp'])-273.15)
        sum+=town_temps
        avg=sum/5
    print ("Average temperature is ",avg)
        
average()  
def  coldest():
 mintemp=9000
 coldesttown=" "
 for i in range(5):
   api_data=apilinks[i].json()
   town_temps=((api_data['main']['temp'])-273.15)
   if town_temps<mintemp:mintemp=town_temps
   if mintemp==town_temps:coldesttown=api_data['name']
 print("Coldest town is:",coldesttown)
  
coldest()
location=input()
complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=f24acb33b0bcc507760fec5abaa0313a"
api_link=requests.get(complete_api_link)
api_data=api_link.json()
#print (api_data)
if api_data['cod']=='404':print("Wrong city{}",format(location))
else:
    town_temps=((api_data['main']['temp'])-273.15) 
    weather=(api_data['weather'][0]['description'])
    hmdt=api_data['main']['humidity']

print("Temp: {}".format(town_temps))
print("Weather Description: ",weather)
print("Humidity: ",hmdt,'%')


