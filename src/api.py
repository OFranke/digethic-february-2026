from flask import Flask, Response, request
from flask_cors import CORS
import pandas as pd
import os
import pickle

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def root():
    return {"hello": "world!!!!"}


@app.route("/hello_world", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/training_data", methods=["GET"])
def training_data():
    training_data = pd.read_csv(os.path.join("data", "auto-mpg.csv"))
    return Response(training_data.to_json(), mimetype="application/json")


file_to_open = open(os.path.join("data", "models", "baummethoden_lr.pickle"), "rb")
trained_model = pickle.load(file_to_open)
file_to_open.close()


@app.route("/predict", methods=["GET"])
def predict():
    zylinder = float(request.args.get("zylinder"))
    ps = float(request.args.get("ps"))
    gewicht = float(request.args.get("gewicht"))
    beschleunigung = float(request.args.get("beschleunigung"))
    baujahr = float(request.args.get("baujahr"))

    print(
        f"Received request with zylinder: {zylinder}, ps: {ps}, gewicht: {gewicht}, beschleunigung: {beschleunigung}, baujahr: {baujahr}"
    )

    prediction_data = [[zylinder, ps, gewicht, beschleunigung, baujahr]]

    prediction = trained_model.predict(prediction_data)

    return {"result": prediction[0]}
