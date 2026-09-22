import joblib
import pandas as pd

# Load trained model
model = joblib.load("asthmaguard_model.pkl")


def predict_risk(heart_rate, spo2, temperature, activity):

    data = pd.DataFrame(
        [[
            heart_rate,
            spo2,
            temperature,
            activity
        ]],
        columns=[
            "heart_rate",
            "spo2",
            "temperature",
            "activity"
        ]
    )

    prediction = model.predict(data)[0]

    if prediction == 1:
        return "HIGH"
    else:
        return "LOW"


# Demo
risk = predict_risk(
    heart_rate=105,
    spo2=94,
    temperature=36.8,
    activity=0
)

print("Risk Level:", risk)