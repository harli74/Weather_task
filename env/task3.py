from flask import Flask,render_template
import random
import time
import requests
import json
from apifuncs import locationcodes,average,coldest,singletowncheck

app=Flask(__name__)

@app.route('/')
def index():
    locationcodes()
    
    townnumbers,avg=average()
    coldtown=coldest()
    return render_template('index.html')

@app.route('/singletown', methods=['GET','POST'])
def check():
    if request.method=='POST':
        towntemp,weather,hmdt=singletowncheck()
        return '''
                  <h1>Current temperature is {} degrees </h1>
                  <h1>Current weather is {} </h1>
                  <h1>Current humidity is {} % degrees </h1>'''.format(towntemp, weather, hmdt)

@app.route('/coldesttown', methods='POST')
def coldestt():
    coldestt=coldest()
    return '<h1> Coldest town is {} <h1>'.format(coldestt)

@app.route('/calcaverage')
def calculate():
    citycount,avg=average()
    return '<h1> The average temperature of {} cities is {}'.format(citycount,avg)