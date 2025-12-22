🚗 Car Price Prediction & Exploratory Data Analysis

Author: Álvaro Mejía
Project Type: Data Science · Machine Learning · EDA · Streamlit App
Status: Complete (future deployment improvements planned)

📌 Project Overview

This project aims to analyze, explore, and predict car prices using real-world vehicle listing data.
It is an improved and extended version of a project originally developed during the HACKABOSS Data Science bootcamp, with a strong focus on:

- Robust Exploratory Data Analysis (EDA)
- Careful handling of outliers and skewed distributions
- Feature engineering driven by domain logic
- Model interpretability and practical constraints
- A professional Streamlit dashboard for interactive data exploration and price estimation

🎯 Objectives

- Understand the structure and quality of car market data
- Detect and analyze outliers and missing values
- Engineer meaningful features to improve model performance
- Train and compare multiple regression models
- Build an interactive EDA app suitable for technical stakeholders
- Integrate a trained ML model into the Streamlit app

🧠 Key Steps

1. Data Cleaning & Feature Engineering

- Log-transformations for highly skewed variables (price, mileage, power)
- Creation of derived features such as car_age
- Encoding of categorical variables (e.g. transmission)
- Careful analysis of numerical variables that behave categorically

2. Outlier Analysis

- Identification of extreme values using Tukey’s fences
- Explicit decision to analyze, not blindly remove outliers
- Understanding their impact on both EDA and model performance

3. Modeling

- Tested models:

    - Random Forest Regressor

    - Gradient Boosting

    - K-Nearest Neighbors

    - Decision Tree

- Evaluation using MAE, RMSE, and R²

- Model trained on a reduced feature set to balance:

- Performance

- Interpretability

- Model size constraints

4. Streamlit Application

- Interactive variable selection
- Hue-based visual grouping (brand, body type, etc.)
- Advanced filters (emissions, transmission, body type)
- Correlation analysis with dynamic variable selection
- Outlier & missing value visualization
- Download filtered datasets
- Model usage tab: users can estimate car price using the trained model

🛠️ Tools & Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Plotly
- Streamlit
- Git & GitHub

⚠️ Notes & Limitations

The trained model is relatively large due to ensemble methods.

Deployment via FastAPI/Docker is planned as a future improvement.

Model training was optimized to balance computation time and performance.