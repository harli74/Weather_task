# ## [Task 1](#task1). Weather API requests - основи

# Да се напише програма, която:

#   * Да показва какво е времето в момента за 5 произволно избрани града (*бонус точки*: град от цял свят, няма ограничение - освен да е написан на латиница):
# 	* Дали е облачно/вали или е слънчево ? 
# 	* Каква е температурата в момента ?
# 	* Каква е влажността в момента ?

# * Да се изведе следните статистики:
# 	* Най-студен град (от избраните 5)
# 	* Средна температура (от избраните 5)

# * **Да може да се въвежда име на град и индивидуално да изкарва статистика:** (бонус точки)
# 	* Облачно ли е ?
# 	* Каква е температурата ?
# 	* Каква е влажността в момента ?


# + Нужни неща:
# 	- Обработване на JSON данни
# 	- HTTP/HTTPS Requests
# 	- Random generator
# 	- User Input
# 	- http://openweathermap.org/api

#apikey: 07cf9f3accb7195ab333a8b337f932d8

import string
import requests
import json
import random

print("Start")
with open('city.list.json','r') as f:
    cityData = json.load(f)

print(type(cityData))
cityer = input()

apikey="c9a787290254e2833d876e34bbccb790"
URL=f"https://api.openweathermap.org/data/2.5/weather?"
key = "q="
end = "&appid="
apiRequest = URL + key + cityer + end + apikey + '&units=metric'
ApiOutput = requests.get(apiRequest)
#Print succesful Access
print(ApiOutput)

data = ApiOutput.json()
Main = data['main']
Weather = data['weather']

print(f"Weather Report: {Weather[0]['description']}")
print(f"Temperature is: {Main['temp']}")
print(f"Humidity is: {Main['humidity']}")

# city = []

# for x in range(5):

#      city.append(input())
    

# print(city) 


