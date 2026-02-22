try:
    import mysql.connector
    print("Se importo MySQL")
except ModuleNotFoundError as e:
    print("No se importo correctamente",
e)

def conexion():
    """
    Docstring for conexion
    Crea la conexion con la base de datos
    Return:
    retorna la variable conn, representa la conexion
    """
    conn = mysql.connector.connect(
        host="db",
        user="botuser",
        password="botpass",
        database="bot"
    )
    print("Se creo la conexion con la base de datos")
    return conn