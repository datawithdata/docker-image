# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:29:23 2022

@author: viswateja
"""

import pickle


def load_model():
    loaded_model = pickle.load(open("finalized_model.sav", 'rb'))
    return loaded_model

def predict(loaded_model,data):
    result = loaded_model.predict(data,)
    return result

def input_req(data):
    model = load_model()
    response = predict(model,data)
    return {"target_names":str(response[0])}


