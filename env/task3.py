from flask import Flask
import random
import time
import requests
import json

app=Flask(__name__)
@app.route('/')
def index():
    url='https://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid=8bd428589520ff3bfe675be56c83d503'

    req=requests.get(url.format(id)).json()

    resp={ 'city' : req['name'],
           'temperature' :req['main']['temp'],
           'humidity' : req['main']['humidity'],
           'description' : req['weather']['description'],
        }
    return '<h1>Hello World</h1>'

def single():
    url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=8bd428589520ff3bfe675be56c83d503'

    req=requests.get(url.format(cityname)).json()

    resp={ 'city' : req['name'],
           'temperature' :req['main']['temp'],
           'humidity' : req['main']['humidity'],
           'description' : req['weather']['description'],
        }