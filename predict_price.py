import joblib

model = joblib.load("price_model.pkl")

# Wedding = 1
prediction = model.predict([[1, 8, 500]])

print("Predicted Price:", prediction[0])




print(model.predict([[4,4,250]]))