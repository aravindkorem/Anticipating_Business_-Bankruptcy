import numpy as np
import pandas as pd
from flask import Flask,url_for,request,send_from_directory
from flask import render_template
from flask import request
from flask import jsonify
import pickle


app = Flask(__name__)
model = pickle.load(open('models.pkl', 'rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/details")
def show_form():
    return render_template("details.html")

@app.route('/predicts/',methods=["POST" ,"GET"])
def predict():
    
   input_feature=[float(x) for x in request.form.values()]
   x = [np.array(input_feature)]
   print(input_feature)
   names = ["Attr2","Attr51","Attr32","Attr52","Attr34","Attr55","Attr29","Attr6","Attr57","Attr3"]
   data = pd.DataFrame(x, columns=names)
   print(data)
   pred = model.predict(data)
   if pred[0] == 1:
       return render_template('predict.html', predict= "Bussiness is going to get Bankrupt")
   else:
       return render_template('predict.html', predict= "Business is safe ")
    
   
if __name__ == '__main__':
    app.run(debug =True, port = 5000)
