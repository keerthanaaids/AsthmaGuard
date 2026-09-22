import random
import time


def generate_sensor_data():

    heart_rate = random.randint(70, 120)
    spo2 = random.randint(91, 99)
    temperature = round(
        random.uniform(36.3, 37.0),
        1
    )

    activity = random.choice([
        0,
        0,
        1
    ])

    return {
        "heart_rate": heart_rate,
        "spo2": spo2,
        "temperature": temperature,
        "activity": activity
    }


while True:

    sensor = generate_sensor_data()

    print("\n--- SENSOR DATA ---")
    print("Heart Rate:", sensor["heart_rate"])
    print("SpO2:", sensor["spo2"])
    print("Temperature:", sensor["temperature"])
    print("Activity:", sensor["activity"])

    time.sleep(3)