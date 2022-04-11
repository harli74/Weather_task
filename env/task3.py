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
    towntemp,weather,hmdt=singletowncheck()
    townnumbers,avg=average()
    coldtown=coldest()
    return render_template('index.html')