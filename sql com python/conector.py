import mysql.connector

def conection_db():
    conect_db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='livraria'
    )
    return conect_db
