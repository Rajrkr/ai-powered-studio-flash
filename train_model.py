import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("price_data.csv")

service_map = {
    "Wedding": 1,
    "Fashion": 2,
    "Studio": 3,
    "Birthday": 4,
    "Family": 5,
    "Commercial": 6
}

df["Service"] = df["Service"].map(service_map)

X = df[["Service", "Hours", "Photos"]]
y = df["Price"]

model = LinearRegression()

model.fit(X, y)

joblib.dump(model, "price_model.pkl")

print("Model Saved Successfully")