from datetime import datetime


def emergency_alert(
    name,
    risk,
    location="Location sharing enabled"
):

    if risk == "HIGH":

        print("\n" + "=" * 45)

        print("🚨 EMERGENCY ALERT")

        print("=" * 45)

        print("Patient:", name)

        print("Risk: POSSIBLE RESPIRATORY DISTRESS")

        print("Time:",
              datetime.now())

        print("Location:",
              location)

        print("\nPlease check the patient immediately.")

        print("=" * 45)


# Demo
emergency_alert(
    name="Patient",
    risk="HIGH",
    location="Location available"
)