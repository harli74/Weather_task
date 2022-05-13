from cgitb import text
from crypt import methods
from email import message
from encodings import search_function
import imp
from multiprocessing import context
from pyexpat.errors import messages
from random import random
from webbrowser import get
from flask import Flask, flash , render_template ,url_for , request, redirect
import requests
import json
import random

app = Flask(__name__)

city = []
cityInfo =[]
CityTemp =[]
Weather=''
frm = 0
apikey="c9a787290254e2833d876e34bbccb790"
URL=f"https://api.openweathermap.org/data/2.5/weather?"
key = "q="
end = "&appid="

@app.route('/',methods=['GET','POST'])
def index():
    

    if request.method=="POST":
        if request.form['btnName'] == 'inputCity':
            return redirect(url_for('CitySearch'))
       # InputBtn = request.form['inputButton']
        #return render_template('index.html')
        elif request.form['btnName'] == 'cityGen':
            print("POST")
            return redirect(url_for('CityGenerator'))
        elif request.form['btnName'] == 'searching':
            print("fakve")
           
            return render_template('CitySearch')
    return render_template('index.html')         
   
        
  
@app.route('/CityGEN',methods=['GET','POST'])
def CityGenerator():
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
    if request.method=="GET":
        coldestCityOutput=f"The coldest city is: {cityInfo[CityTemp.index(min(CityTemp))]}"
        AverageTemp = f"The average temperature is: {sum(CityTemp) / len(CityTemp)}"
        return render_template('GenerateCities.html',AverageTemp=AverageTemp,coldestCityOutput=coldestCityOutput,cityInfo=cityInfo,CityTemp=CityTemp)  
    else:
        return render_template('GenerateCities.html') 
@app.route('/CitySearch',methods=['GET','POST'])
def CitySearch():
     if request.method=="POST":
        data = request.form.get('Search')
        ApiInputRequest = URL + key + data + end + apikey + '&units=metric'
        ApiRequest_Input = requests.get(ApiInputRequest)
        dataweather = ApiRequest_Input.json()
        Main = dataweather['main']
        Weather = dataweather['weather']
        TextValue1= f"City name: {dataweather['name']} Weather is: {Weather[0]['description']} Temperature: {Main['temp']} Humidity: {Main['humidity']}"
        
        return render_template('CitySearch.html',TextValue1 = TextValue1,data=data)  
     else:
        return render_template('CitySearch.html') 


if __name__ == '__main__':    
    app.run(debug=True)