import json
from joblib import load
from sklearn.linear_model import LinearRegression
import numpy as np

def readFile(filename):
    content = ""

    try:
        with open(filename, 'r') as fileContent:
            content = fileContent.read()
    except Exception as Err:
        print("{}".format(Err))

    return content

def readJson(filename):
    content = {}

    try:
        content = json.loads(readFile(filename))
    except Exception as Err:
        print("{}".format(Err))

    return content   

def predictCrop(N, P, K, temp, hum, pH, rain):
    model = load('modelNB.joblib')
    features = [[N,P,K,temp,hum,pH,rain]]
    features = np.array(features)
    features.reshape(-1,1)
    crop = model.predict(features)
    return crop[0]; 