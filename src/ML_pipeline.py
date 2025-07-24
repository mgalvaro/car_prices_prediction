# this file contains the pipeline to train a reduced and more compact model

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib


def train_reduced_model(
    data_path: str,
    top_features: list,
    target: str = "log_price",
    model_params: dict = None,
    sample_frac: float = 0.5,
    test_size: float = 0.2,
    save_path: str = "../outputs/RandomForest_model.pkl",
    compress: int = 5,
    train_on_full_data: bool = True,
):
    # Load data and optionally sample it
    df = pd.read_csv(data_path)
    df_sample = df.sample(frac=sample_frac, random_state=42, ignore_index=True)

    # Default model parameters if not passed
    if model_params is None:
        model_params = {
            "random_state": 42,
            "n_estimators": 200,
            "min_samples_split": 5,
            "min_samples_leaf": 1,
            "max_features": "sqrt",
            "max_depth": 20,
            "criterion": "absolute_error",
        }

    # Define model
    model = RandomForestRegressor(**model_params)

    # Train-test split
    X = df_sample[top_features]
    y = df_sample[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    # Fit and predict
    model.fit(X_train, y_train)
    y_pred_log = model.predict(X_test)

    # Inverse log if needed
    y_pred = np.expm1(y_pred_log)
    y_test_exp = np.expm1(y_test)

    # Metrics
    metrics = {
        "MAE": mean_absolute_error(y_test_exp, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_test_exp, y_pred)),
        "R2": r2_score(y_test_exp, y_pred),
    }

    print("Validation metrics:")
    print(metrics)

    # Optionally retrain on full data
    # for efficiency, we won't do it in this project, as long as we still get robust metrics
    # if train_on_full_data:
    #     X_full = df[top_features]
    #     y_full = df[target]
    #     model.fit(X_full, y_full)

    # Save final model
    joblib.dump(model, save_path, compress=compress)
    print(f"\n✅ Model saved to: {save_path}")

    return model, metrics
