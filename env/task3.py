from flask import Flask
import random
import time

app=Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World</h1>'