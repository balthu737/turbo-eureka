from bot.telegram_bot import bot
from database.query import Querys
from service.core.mensaje import analisis
from service.core.service import Gasto, Usuarios
from config import TOKEN
query = Querys()
gastos = Gasto()
usuarios = Usuarios()
token = TOKEN

def guardar_gasto(monto, categoria):
    query.insetar_movimiento(1, monto, categoria)

def mensaje(text):
    analisis(text, guardar_gasto)

bot(token, mensaje)