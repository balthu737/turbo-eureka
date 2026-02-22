from bot.telegram_bot import bot
from database.query import Querys
from service.core.mensaje import analisis
from service.core.service import Gasto, Usuarios
from config import TOKEN
query = Querys()
gastos = Gasto()
usuarios = Usuarios()
token = TOKEN

def guardar_gasto(usuario_id, monto, categoria):
    query.insetar_movimiento(usuario_id, monto, categoria)

def mensaje(usuario_id, text, nombre, username):
    query.crear_usuario(usuario_id, nombre, username)
    analisis(usuario_id, text, guardar_gasto)

bot(token, mensaje)