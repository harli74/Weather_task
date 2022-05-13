from cgitb import text
from crypt import methods
from email import message
from encodings import search_function
import imp
from multiprocessing import context
from pyexpat.errors import messages
from webbrowser import get
from flask import Flask, flash , render_template ,url_for , request, redirect
import requests
import SearchFunc

app = Flask(__name__)

city = []
cityInfo =[]
CityTemp =[]
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
    
    return render_template('GenerateCities.html')  
    
@app.route('/CitySearch',methods=['GET','POST'])
def CitySearch():
     if request.method=="POST":
        data = request.form.get('Search')
        print(data)
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