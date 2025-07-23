import mysql
from my_secrets.passwords import password


# this function will work for a local db in mysql
def execute_query(query, pw, database="cars_db", host="localhost", user="root"):

    db = mysql.connector.connect(host=host, user=user, pw=password, database=database)

    cursor = db.cursor()

    cursor.execute(query)

    cursor.fetchall()  # empty cursor
    cursor.close()
    db.close()
