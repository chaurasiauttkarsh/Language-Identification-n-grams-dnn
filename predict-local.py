#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:49:32 2021
@author: uttkarshchaurasia
"""
# Importing the libraries
from tensorflow import keras # keras
import pickle # pickle
import numpy as np #numpy
import re # regular expressions
import pandas as pd # pandas

try:
    model = keras.models.load_model('model/model.h5')
except:
    print("Error : Model not found!!!")
try:
    infile = open('model/parameters.sav','rb')
    train_max, train_min, vectorizer, feature_names, encoder = pickle.load(infile)
except:
    print("Error : Parameters not found!!!")

# Preprocessing each text line
def data_preprocess(text):
    # Removing numbers and symbols
    text = re.sub(r'[!@#$()-_,n"%^*?:;~`0-9]', ' ', text) 
    text = re.sub(r'[[]]', ' ', text)
    # Lowercasing the text
    text = text.lower() 
    return text

# Function to detect language
def detect_language(text):
    text = data_preprocess(text)
    X = vectorizer.fit_transform([text])
    X_feat = pd.DataFrame(data=X.toarray(),columns=feature_names)
    X_feat = (X_feat - train_min)/(train_max-train_min)
    predicted_my_val = model.predict(X_feat)
    val = np.where(predicted_my_val[0] == np.amax(predicted_my_val[0]))[0]
    print("Detected Language :", encoder.classes_[val[0]])
  
my_text = input("Enter the text : ")
my_val = detect_language(my_text)