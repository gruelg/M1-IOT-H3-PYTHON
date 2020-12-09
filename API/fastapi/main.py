from typing import Optional

import joblib
from fastapi import FastAPI
from flask import request

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/{stri}")
def param( stri: str):
    model_filename = "./data/hatespeech.joblib.z"
    clf = joblib.load(model_filename)
    # Receives the input query from form
    probas = clf.predict_proba([stri])[0]
    return {"Hate speech : ": probas[0], "Offensive language : ": probas[1], "Neither : ": probas[2]}