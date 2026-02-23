from database.conexcion import conexion
import pandas as pd
class   Querys():
    def insetar_movimiento(self, usuario_id, amount, category_id):
        conn = conexion()
        cursor = conn.cursor()
        id = self.id_categoria(category_id)
        query = f'INSERT INTO movimiento (usuario_id, monto, categoria_id, fecha) VALUES ({usuario_id}, {amount}, {id}, NOW())'
        cursor.execute(query)
        cursor.close()
        conn.commit()
        conn.close()
        print("Se añadio el gasto de forma correcta...")
    def crear_usuario(self, user_id, nombre, username):
        conn = conexion()
        cursor = conn.cursor()
        query = f'SELECT * FROM usuarios WHERE usuario_id = {user_id}'
        cursor.execute(query)
        result = cursor.fetchall()
        if not result:
            insert_query = f'''
            INSERT INTO usuarios (usuario_id, nombre, username)
            VALUES ({user_id}, "{nombre}", "{username}")
            '''
            cursor.execute(insert_query)
            print("Usuario registrado correctamente...")
        else:
            print("Usuario ya existente")
        conn.commit()
        cursor.close()
        conn.close()
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
            categoria_id = resultado[0][0]
            cursor.close()
            conn.close()
            return categoria_id
        cursor.execute(query_2)
        conn.commit()
        categoria_id = cursor.lastrowid
        cursor.close()
        cursor.close()
        return categoria_id
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