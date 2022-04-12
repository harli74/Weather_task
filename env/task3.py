from flask import Flask, render_template, request, url_for, redirect
import random
import time
import requests
import json
from apifuncs import locationcodes,average,coldest,singletowncheck

app=Flask(__name__)

@app.route('/')
def index():
    locationcodes()
    return render_template('index.html')

@app.route('/singletown', methods=['GET','POST'])
def check():
    if request.method=='POST':
        if(request.form.get('activate')=='activate'):
            city=request.form.get('srch')
            towntemp,weather,hmdt=singletowncheck(city)
        return '''
                  <h1>Current temperature is {} degrees </h1>
                  <h1>Current weather is {} </h1>
                  <h1>Current humidity is {} % degrees </h1>'''.format(towntemp, weather, hmdt)
    return render_template('singletown.html')

@app.route('/coldesttown', methods=['GET', 'POST'])
def coldestt():
    coldestt=coldest()
    return '<h1> Coldest town is {} <h1>'.format(coldestt)

@app.route('/calcaverage')
def calculate():
    citycount,avg=average()
    return '<h1> The average temperature of {} cities is {}'.format(citycount,avg)

if __name__=="__main__":
    app.run(debug=True)