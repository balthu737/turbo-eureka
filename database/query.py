from database.conexcion import conexion
from datetime import datetime
class Querys():
    def insetar_movimiento(self, usuario_id, amount, category_id=None, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = conexion()
        cursor = conn.cursor()
        query = f'INSERT INTO movimientos (people_id, amount, category_id, date) VALUES ({usuario_id}, {amount}, {category_id}, "{date}")'
        cursor.execute(query)
        cursor.close()
        conn.close()
        print("Se añadio el gasto de forma correcta...")
    def crear_usuario(self, user_name, first_name, email=None):
        conn = conexion()
        cursor = conn.cursor()
        query = f'INSERT INTO usuarios (user_name, first_name, email) VALUES ({user_name}, {first_name}, {email})'
        cursor.execute(query)
        cursor.close()
        conn.close()
        print("Se registro el usuario de forma correcta...")
    def hoy(self):
        conn = conexion()
        cursor = conn.cursor(dictionary=True)
        query = f''
        cursor.execute(query)
        dato = cursor.fetchall()
        cursor.close()
        conn.close()
        print(f'''Se hizo la consulta de forma correcta los datos son:
{dato}''')
        return dato
    def semana(self):
        conn = conexion()
        cursor = conn.cursor(dictionary=True)
        query = f''
        cursor.execute(query)
        dato = cursor.fetchall()
        cursor.close()
        conn.close()
        print(f'''Se hizo la consulta de forma correcta los datos son:
{dato}''')
        return dato
    def mes(self):
        conn = conexion()
        cursor = conn.cursor(dictionary=True)
        query = f''
        cursor.execute(query)
        dato = cursor.fetchall()
        cursor.close()
        conn.close()
        print(f'''Se hizo la consulta de forma correcta los datos son:
{dato}''')
        return dato
    def anio(self):
        conn = conexion()
        cursor = conn.cursor(dictionary=True)
        query = f''
        cursor.execute(query)
        dato = cursor.fetchall()
        cursor.close()
        conn.close()
        print(f'''Se hizo la consulta de forma correcta los datos son:
{dato}''')
        return dato