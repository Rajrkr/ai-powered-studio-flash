import pandas as pd
import joblib

model = joblib.load("package_model.pkl")

data = pd.DataFrame({
    "Budget": [15000],
    "Event": [3]
})

prediction = model.predict(data)

print("Recommended Package:", prediction[0])