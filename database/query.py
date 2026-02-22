from database.conexcion import conexion
from datetime import datetime
import pandas as pd
class   Querys():
    def insetar_movimiento(self, usuario_id, amount, category_id, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = conexion()
        cursor = conn.cursor()
        id = self.id_categoria(category_id)
        query = f'INSERT INTO movimiento (usuario_id, monto, categoria_id, fecha) VALUES ({usuario_id}, {amount}, {id}, "{date}")'
        cursor.execute(query)
        cursor.close()
        conn.commit()
        conn.close()
        print("Se añadio el gasto de forma correcta...")
    def crear_usuario(self, user_name, first_name, email=None):
        conn = conexion()
        cursor = conn.cursor()
        query = f'INSERT INTO usuarios (user_name, first_name, email) VALUES ({user_name}, {first_name}, {email})'
        cursor.execute(query)
        cursor.close()
        conn.commit()
        conn.close()
        print("Se registro el usuario de forma correcta...")
    def ver_categorias(self):
        conn = conexion()
        query = f'SELECT * FROM categoria'
        df = pd.read_sql(query, conn)
        print(f"""
Listando tabla de categorias:
{df}
""")
        return df
    def id_categoria(self, categoria):
        conn = conexion()
        cursor = conn.cursor()
        query = f'SELECT id FROM categoria WHERE nombre = "{categoria}"'
        query_2 = f'INSERT INTO categoria (nombre) VALUES ("{categoria}")'
        cursor.execute(query)
        resultado = cursor.fetchall()
        if resultado:
            return resultado[0]
        cursor.execute(query_2)
        conn.commit()
        return cursor.lastrowid
    def hoy(self):
        conn = conexion()
        query = f''
        df = pd.read_sql(query, conn)
        print(f'''Se hizo la consulta de forma correcta los datos son:
{df}''')
        return df
    def semana(self):
        conn = conexion()
        query = f''
        df = pd.read_sql(query, conn)
        print(f'''Se hizo la consulta de forma correcta los datos son:
{df}''')
        return df
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
        query = f''
        df = pd.read_sql(query, conn)
        print(f'''Se hizo la consulta de forma correcta los datos son:
{df}''')
        return df