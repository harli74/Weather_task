from crypt import methods
from webbrowser import get
from flask import Flask , render_template ,url_for , request, redirect


app = Flask(__name__)

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
    return render_template('index.html')         
   
        
  
@app.route('/CityGEN',methods=['GET','POST'])
def CityGenerator():
    return render_template('GenerateCities.html')  
    
@app.route('/CitySearch',methods=['GET','POST'])
def CitySearch():
    return render_template('CitySearch.html')  


if __name__ == '__main__':    app.run(debug=True)