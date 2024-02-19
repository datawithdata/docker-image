# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:35:22 2022

@author: viswateja
"""

from flask import Flask,request
from predit import input_req
app = Flask(__name__)

@app.route('/predict',methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        data=request.get_json()
        print("-----------",data)
        res=input_req(data['data'])
    return res

# main driver function
if __name__ == '__main__':
 
	app.run(debug=True)
