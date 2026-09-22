import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("ai_model/dataset.csv")

# Input features
X = data[
    [
        "heart_rate",
        "spo2",
        "temperature",
        "activity"
    ]
]

# Target
y = data["risk"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Test
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Save model
joblib.dump(model, "asthmaguard_model.pkl")

print("\nModel saved successfully!")