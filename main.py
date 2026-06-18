from fastapi import FastAPI
from pydantic import BaseModel
import joblib
 
app = FastAPI()
model = joblib.load("model.joblib")           # loaded ONCE
labels = ["setosa", "versicolor", "virginica"]
 
# Pydantic model = automatic input validation
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width:  float
    petal_length: float
    petal_width:  float
 
@app.post("/predict")
def predict(data: IrisInput):
    features = [[data.sepal_length, data.sepal_width,
                 data.petal_length, data.petal_width]]
    pred = model.predict(features)[0]
    return {"prediction": labels[pred]}
