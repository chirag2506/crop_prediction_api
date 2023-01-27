import os, uvicorn
from appUtils import *
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
configFile = "config/app.setting.json"
configuration = readJson(configFile)

@app.get("/")
async def default():
    return JSONResponse({
            "Hello":"Welcome to Crop Prediction API"
    })

@app.get("/predict/")
async def predict(n: float, p: float, k: float, temp: float, hum: float, ph: float, rain: float):
    prediction = predictCrop(n, p, k, temp, hum, ph, rain)
    return JSONResponse({
        "Prediction": prediction
    })


if __name__ == '__main__':
    uvicorn.run(app,
                host=configuration["App"]["Host"],
                port=configuration["App"]["Port"])