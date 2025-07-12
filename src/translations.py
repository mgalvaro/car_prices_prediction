# Here, the mappings for the raw data translations from Spanish to English are included
# These are lists or dictionaries that are used to translate the raw data and the columns' names

import numpy as np

# These are the translations of the columns names
columns_names = [
    "registration_date",  # Fecha de matriculación
    "fuel_type_1",  # Combustible
    "mileage_km",  # Kilómetros
    "body_type_1",  # Carrocería
    "transmission",  # Cambio
    "power_hp",  # Potencia (cv)
    "warranty_months",  # Garantía
    "color",  # Color
    "emissions_label",  # Distintivo ambiental
    "price",  # precio
    "url",  # url
    "length_mm",  # largo
    "width_mm",  # ancho
    "height_mm",  # alto
    "wheelbase_mm",  # batalla_mm
    "trunk_volume_l",  # maletero_l
    "weight_kg",  # peso_masa_kg
    "body_type_2",  # carroceria
    "doors",  # puertas
    "seats",  # plazas
    "fuel_type_2",  # combustible
    "engine_displacement_cm3",  # cilindrada_cm3
    "cylinders",  # cilindros
    "turbo",  # sobrealimentacion
    "consumption_city_l_100km",  # urbano
    "consumption_highway_l_100km",  # carretera
    "consumption_mixed_l_100km",  # medio
    "co2_g_km",  # co2
    "tank_capacity_l",  # deposito
]

# cars' fuel type 1 & 2
fuel_type_1_mapping = {
    "Gasolina": "Petrol",
    "Corriente eléctrica": "Electric",
    "Eléctrico": "Electric",
    "Diésel": "Diesel",
    "Diesel": "Diesel",
    "Híbrido": "Hybrid",
    "Gasolina y corriente eléctrica": "Plug-in Hybrid Petrol/Electric",
    "Híbrido Enchufable": "Plug-in Hybrid",
    "Diesel y corriente eléctrica": "Plug-in Hybrid Diesel/Electric",
    "Gasolina/gas": "Petrol/Gas",
    "Gas": "Gas",
    "Mixto Gasolina/Etanol": "Petrol/Ethanol",
    np.nan: np.nan,  # Mantener los NaN como están
}

fuel_type_2_mapping = {
    "Corriente eléctrica": "Electric",
    "Gasolina": "Petrol",
    "Diesel": "Diesel",
    "Gasolina y corriente eléctrica": "Plug-in Hybrid Petrol/Electric",
    "Gasolina/gas": "Petrol/Gas",
    "Diesel y corriente eléctrica": "Plug-in Hybrid Diesel/Electric",
    "Mixto Gasolina/Etanol": "Petrol/Ethanol",
    np.nan: np.nan,
}


# body type 1 & 2
body_type_1_mapping = {
    "Berlina mediana o grande": "Sedan",
    "Berlina": "Sedan",
    "Pequeño": "Small",
    "Convertible": "Convertible",
    "Todo Terreno": "SUV",
    "4x4, SUV o pickup": "SUV/Pickup",
    "Deportivo o coupé": "Coupe/Sports",
    "Coupe": "Coupe",
    "Descapotable o convertible": "Convertible",
    "Roadster": "Roadster",
    "Familiar": "Estate",
    "Stationwagon": "Estate",
    "Monovolumen": "MPV",
    "Coche clásico": "Classic",
    "Combi": "Estate",
    "Targa": "Targa",
    "Pick-Up Doble Cabina": "Pickup",
    "Pick-Up": "Pickup",
    "Industrial": "Commercial",
    "-": np.nan,
    np.nan: np.nan,
}

body_type_2_mapping = {
    "Berlina": "Sedan",
    "Convertible": "Convertible",
    "Todo Terreno": "SUV",
    "Coupe": "Coupe",
    "Roadster": "Roadster",
    "Stationwagon": "Estate",
    "Monovolumen": "MPV",
    "Combi": "Estate",
    "Targa": "Targa",
    "Pick-Up Doble Cabina": "Pickup",
    "Pick-Up": "Pickup",
    np.nan: np.nan,
}

# transmission
transmission_mapping = {"Manual": "Manual", "Automático": "Automatic", np.nan: np.nan}

# turbo
turbo_mapping = {
    "Turbo": "Turbo",
    "Turbo de geometría variable": "Variable geometry turbo",
    "Doble turbo": "Twin-turbo",
    "Tipo de sobrealimentador": "Type of forced induction",
    "Compresor y turbo": "Supercharger and turbo",
    "Compresor Lisholm": "Lysholm supercharger",
    "Compresor de raices": "Roots supercharger",
    "-": "Not specified",
    np.nan: np.nan,
}
