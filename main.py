from bot.telegram_bot import bot
from database.query import Querys
from service.core.mensaje import analisis
from service.core.service import Gasto, Usuarios

query = Querys()
gastos = Gasto()
usuarios = Usuarios()
TOKEN = "8017156472:AAFQbaQNjtlhS2KCe9W_4-MxCR-2Wm9CKRc"

def guardar_gasto(monto, categoria):
    query.insetar_movimiento(1, monto, categoria)

def mensaje(text):
    analisis(text, guardar_gasto)

bot(TOKEN, mensaje)