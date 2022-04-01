import requests
 
location=input("Enter City Name:")
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


