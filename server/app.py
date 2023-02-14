from fastapi import FastAPI
from pydantic import BaseModel, conlist
from joblib import load
import ast

flower_type = {"Setosa": "images/setosa.jpg", "Versicolor" : "images/versicolor.jpg", "Virginica" : "images/virginica.jpg"}

# Charger le modèle
model = load('iris_ML_v1.joblib')

app = FastAPI(title="Iris ML API",
    description="API for iris dataset ml model", version="1.0")

class Iris(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float

@app.get("/")
def read_root():
    return {"ML API"}

@app.post('/predict', tags=["predictions"])

async def get_prediction(iris: Iris):
    # Doit modifier to ast.literal_eval pour convertir une class str to dict
    data = ast.literal_eval(iris.json())
    values = [[data["sepal_length"], data["sepal_width"], data["petal_length"], data["petal_width"]]]
    prediction = model.predict(values).tolist()

# !!! prediction[0] est très important sinon cela renvoie une clé-valeur et non la valeur
    path = flower_type[prediction[0]]
    
 # !!! prediction[0] est très important sinon cela renvoie une clé-valeur et non la valeur
    return {"prediction": prediction[0], "image" : path}
