import numpy as np
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

# Load model
model = joblib.load(f"{BASE_DIR}/reduced_RF_model.pkl")

# this is the pipeline to get the parameters, run the model and get the prediction
def run_model(car_age, power_hp, mileage_km, transmission_auto):
    # Calculate required features
    log_power_hp = np.log1p(power_hp)
    log_mileage_km = np.log1p(mileage_km)
    transmission_auto_binary = 1 if transmission_auto == "Automatic" else 0

    # Build input array
    input_array = np.array(
        [[car_age, transmission_auto_binary, log_power_hp, log_mileage_km]]
    )

    # Predict log price
    predicted_log_price = model.predict(input_array)[0]

    # Convert back to price
    predicted_price = np.expm1(predicted_log_price)

    return predicted_price
