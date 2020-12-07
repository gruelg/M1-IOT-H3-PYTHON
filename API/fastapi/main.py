from typing import Optional

import joblib
from fastapi import FastAPI
from flask import request

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/param/{str}")
def param( str: str):
    model_filename = "./data/hatespeech.joblib.z"
    clf = joblib.load(model_filename)
    # Receives the input query from form
    namequery = str
    data = [namequery]
    probas = clf.predict_proba([str(data)])[0]
    return {"q": probas}