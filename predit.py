# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:29:23 2022

@author: viswateja
"""

import pickle
file_path = "config.json"
with open(file_path, "r") as file:
    contents = json.loads(file.read())

def load_model():
    loaded_model = pickle.load(open(contents['model_name'], 'rb'))
    return loaded_model

def predict(loaded_model,data):
    result = loaded_model.predict(data,)
    return result

def input_req(data):
    model = load_model()
    response = predict(model,data)
    return {"flower_names":str(response[0])}


