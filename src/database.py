import mysql.connector
from src.passwords import password
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


# this function will work for a local db in mysql
# Create a passwords.py file in src and store there your password
def execute_query(
    query, pw=password, database="cars_data", host="localhost", user="root"
):

    db = mysql.connector.connect(host=host, user=user, password=pw, database=database)

    cursor = db.cursor()

    cursor.execute(query)

    cursor.fetchall()  # empty cursor
    cursor.close()
    db.close()


# insert data
def insert_to_table(
    data,
    table="cars",
    database="cars_data",
    host="localhost",
    user="root",
    password=password,
):

    # Get column names from the DataFrame (skip the auto-incremented ID if present)
    column_names = data.columns.tolist()

    # Prepare the INSERT query
    insert_query = f"""
    INSERT INTO {table} ({', '.join(column_names)})
    VALUES ({', '.join(['%s'] * len(column_names))})
    """

    # Convert DataFrame rows to list of tuples
    values = [tuple(row[col] for col in column_names) for _, row in data.iterrows()]

    # Connect and execute
    db = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )
    cursor = db.cursor()

    cursor.executemany(insert_query, values)
    db.commit()
    print(f"Added: {cursor.rowcount} filas")

    cursor.close()
    db.close()

    # try:
    #     cursor.executemany(insert_query, values)
    #     db.commit()
    #     print(f"Added: {cursor.rowcount} filas")
    # except mysql.connector.Error as err:
    #     print(f"⚠️ MySQL error: {err}")
    #     db.rollback()
    # finally:
    #     cursor.close()
    #     db.close()


def insert_df_sqlalchemy(
    df,
    table="cars",
    database="cars_data",
    host="localhost",
    user="root",
    password=password,
):
    # Replace NaNs with None to allow NULLs in SQL
    df_clean = df.applymap(lambda x: None if pd.isna(x) else x)

    # Create SQLAlchemy connection string
    connection_str = f"mysql+pymysql://{user}:{password}@{host}/{database}"

    # Create engine
    engine = create_engine(connection_str)

    # Use pandas to_sql method (will create the table if it doesn’t exist)
    df_clean.to_sql(table, con=engine, if_exists="append", index=False)

    print(f"✅ Inserted {len(df_clean)} rows into '{table}' table.")
