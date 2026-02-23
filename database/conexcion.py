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
        host=os.getenv("MYSQLHOST"),
        port = int(os.getnv("MYSQLPORT")),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE")
    )
    print("Se creo la conexion con la base de datos")
    return conn