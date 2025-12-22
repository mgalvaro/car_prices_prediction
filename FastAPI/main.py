from fastapi import FastAPI
from pydantic import BaseModel
from ML_model.run_model import run_model

# declare the API
app = FastAPI()


# define the data type of the parameters to ensure data validation
class CarFeatures(BaseModel):
    car_age: float
    transmission_type: str
    mileage_km: float
    power_hp: float


# define the output model
class Price(BaseModel):
    predicted_price: float


# simple get to check that the erver is running
@app.get("/")
def home():
    return {"health_check": "OK"}


@app.post("/predict", response_model=Price)
def predict(features: CarFeatures):
    prediction = round(
        run_model(
            features.car_age,
            features.power_hp,
            features.mileage_km,
            features.transmission_type,
        ),
        2,
    )
    return {"predicted_price_euros": prediction}
