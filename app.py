# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:35:22 2022

@author: viswateja
"""

from flask import Flask,request
from predict import input_req
app = Flask(__name__)

@app.route('/predict',methods=['POST', 'GET'])
def predict():
    response=input_req(request.get_json())
    return "success"

@app.route('/health',methods=['POST', 'GET'])
def health():
    return "Success"

# main driver function
if __name__ == '__main__':
 
	app.run(debug=True)
