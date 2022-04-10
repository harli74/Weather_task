from flask import Flask
import random
import time
import requests
import json
from apifuncs import locationcodes,average,coldest,singletowncheck
codelist=[]
app=Flask(__name__)

@app.route('/')

def generate():
    with open('city.list.json',encoding='UTF-8') as json_file:
        data = json.load(json_file)
        for i in data:
            codelist.append(i['id'])
        random.shuffle(codelist)
        print(codelist)

@app.route('/average')        
def average():
    sum=0
    maxtowns=random.randint(20,40)
    url='https://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid=8bd428589520ff3bfe675be56c83d503'
    
    for i in range(0,maxtowns):
        req=requests.get(url.format(codelist[i])).json()
        time.sleep(0.32)
        sum+=req[i]['temp']
    return sum/maxtowns

@app.route('/singletown')
def single():
    url='https://api.openweathermap.org/data/2.5/weather?q={cityname}&units=metric&appid=8bd428589520ff3bfe675be56c83d503'

    req=requests.get(url.format(cityname)).json()

    resp={ 'city' : req['name'],
           'temperature' :req['main']['temp'],
           'humidity' : req['main']['humidity'],
           'description' : req['weather']['description'],
           
        }
    return resp