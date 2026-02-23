try:
    import mysql.connector
    print("Se importo MySQL")
except ModuleNotFoundError as e:
    print("No se importo correctamente",
e)
import os
def conexion():
    """
    Docstring for conexion
    Crea la conexion con la base de datos
    Return:
    retorna la variable conn, representa la conexion
    """
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    print("Se creo la conexion con la base de datos")
    return conn