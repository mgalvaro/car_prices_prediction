CREATE DATABASE IF NOT EXISTS cars_data;
USE cars_data;

CREATE TABLE IF NOT EXISTS cars (
    car_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    fuel_type VARCHAR(255),
    mileage_km FLOAT,
    body_type VARCHAR(255),
    transmission VARCHAR(255),
    power_hp FLOAT,
    warranty_months FLOAT,
    emissions_label VARCHAR(255),
    price FLOAT,
    length_mm FLOAT,
    width_mm FLOAT,
    height_mm FLOAT,
    wheelbase_mm FLOAT,
    weight_kg FLOAT,
    doors FLOAT,
    seats FLOAT,
    engine_displacement_cm3 FLOAT,
    cylinders FLOAT,
    turbo VARCHAR(10),
    consumption_city_l_100km FLOAT,
    consumption_highway_l_100km FLOAT,
    consumption_mixed_l_100km FLOAT,
    co2_g_km FLOAT,
    tank_capacity_l FLOAT,
    registration_month INT,
    registration_year INT,
    trunk_dim_1 FLOAT,
    trunk_dim_2 FLOAT
);
