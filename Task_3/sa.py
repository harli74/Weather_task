from random import random
from webbrowser import get
from flask import Flask, flash , render_template ,url_for , request, redirect
import requests
import json
import random

app = Flask(__name__)

city = []
city_info =[]
city_temp =[]
apikey="c9a787290254e2833d876e34bbccb790"
URL=f"https://api.openweathermap.org/data/2.5/weather?"
key = "q="
end = "&appid="

@app.route('/',methods=['GET','POST'])
def index():
    

    if request.method=="POST":
        if request.form['btn_name'] == 'input_city':
            return redirect(url_for('CitySearch'))
       # InputBtn = request.form['inputButton']
        #return render_template('index.html')
        elif request.form['btn_name'] == 'city_gen':
            print("POST")
            return redirect(url_for('CityGenerator'))
        elif request.form['btn_name'] == 'searching':
            
           
            return render_template('CitySearch')
    return render_template('index.html')         
   
        
  
@app.route('/CityGEN',methods=['GET','POST'])
def CityGenerator():
    city.clear()
    city_info.clear()
    city_temp.clear()
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
    if request.method=="GET":
        coldest_city_output=f"The coldest city is: {city_info[city_temp.index(min(city_temp))]}"
        average_temp = f"The average temperature is: {sum(city_temp) / len(city_temp)}"
        return render_template('GenerateCities.html',average_temp=average_temp,coldest_city_output=coldest_city_output,city_info=city_info,city_temp=city_temp)  
    else:
        return render_template('GenerateCities.html') 
@app.route('/CitySearch',methods=['GET','POST'])
def CitySearch():
     if request.method=="POST":
        data = request.form.get('Search')
        api_input_request = URL + key + data + end + apikey + '&units=metric'
        api_request_input = requests.get(api_input_request)
        dataweather = api_request_input.json()
        main = dataweather['main']
        weather = dataweather['weather']
        text_value_1= f"City name: {dataweather['name']} Weather is: {weather[0]['description']} Temperature: {main['temp']} Humidity: {main['humidity']}"
        
        return render_template('CitySearch.html',text_value_1 = text_value_1,data=data)  
     else:
        return render_template('CitySearch.html') 


if __name__ == '__main__':    
    app.run(debug=True)