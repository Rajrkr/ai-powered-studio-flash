import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

df = pd.read_csv("package_data.csv")

event_map = {
    "Fashion": 1,
    "Birthday": 2,
    "Wedding": 3,
    "Studio": 4,
    "Family": 5,
    "Commercial": 6
}

df["Event"] = df["Event"].map(event_map)

X = df[["Budget", "Event"]]
y = df["Package"]

model = DecisionTreeClassifier()

model.fit(X, y)

joblib.dump(model, "package_model.pkl")

print("Package Model Saved")