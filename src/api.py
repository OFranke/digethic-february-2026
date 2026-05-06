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
