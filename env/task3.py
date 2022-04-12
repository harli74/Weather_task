from flask import Flask, render_template, request, url_for, redirect
import random
import time
import requests
import json
from apifuncs import locationcodes,average,coldest,singletowncheck

app=Flask(__name__)

#@app.route('/')
#def index():
    
    #return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def check():
    locationcodes()
    if request.method=='POST':
        #if(request.form.get('srch')!=null):
            city=request.form.get('city')
            towntemp,weather,hmdt=singletowncheck(city)
            data1={"city": city,"towntemp": towntemp,"weather": weather,"hmdt": hmdt}
    
            return render_template('index.html' , data1=data1)
def calculate():
    if request.method=='POST':
        citycount,avg=average()
        coldestt=coldest()
        return render_template('index.html', citycount=citycount, avg=avg, cold=coldestt)
#elif(request.form.get('coldest')=='coldest'):
            #coldestt=coldest()
            #return '<h1> Coldest town is {} <h1>'.format(coldestt)
      #elif(request.form.get('average')=='average'):
            #citycount,avg=average()
            #return '<h1> The average temperature of {} cities is {}'.format(citycount,avg)
    #return render_template('index.html')

#@app.route('/coldesttown', methods=['GET', 'POST'])
#
    #return '<h1> Coldest town is {} <h1>'.format(coldestt)

#@app.route('/calcaverage')


if __name__=="__main__":
    app.run(debug=True)