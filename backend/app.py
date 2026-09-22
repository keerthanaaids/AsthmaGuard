from flask import Flask, request, jsonify
from flask_cors import CORS

import sys
import os

# Allow importing AI model
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../ai_model"
        )
    )
)

from predict import predict_risk


app = Flask(__name__)

CORS(app)


@app.route("/")
def home():

    return {
        "message": "AsthmaGuard Backend Running"
    }


@app.route(
    "/sensor-data",
    methods=["POST"]
)
def sensor_data():

    data = request.json

    heart_rate = data["heart_rate"]
    spo2 = data["spo2"]
    temperature = data["temperature"]
    activity = data["activity"]

    risk = predict_risk(
        heart_rate,
        spo2,
        temperature,
        activity
    )

    return jsonify({

        "heart_rate": heart_rate,
        "spo2": spo2,
        "temperature": temperature,
        "activity": activity,
        "risk": risk

    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )