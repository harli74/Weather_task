from flask import Flask, render_template, request, url_for, redirect
import random
import time
import requests
import json
from apifuncs import locationcodes,average,coldest,singletowncheck

app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def check():
    locationcodes()
    if request.method=='POST':
            city=request.form.get('city')
            towntemp,weather,hmdt=singletowncheck(city)
            data1={"city": city,"towntemp": towntemp,"weather": weather,"hmdt": hmdt}
            citycount,avg=average()
            coldestt=coldest()
            return render_template('index.html' , data1=data1, citycount=citycount, avg=avg, cold=coldestt)
    
if __name__=="__main__":
    app.run(debug=True)