from bot.telegram_bot import bot
from database.query import Querys
from service.core.mensaje import message_handler
from service.core.service import Gasto, Usuarios

query = Querys()
gastos = Gasto()
usuarios = Usuarios()
TOKEN = "8017156472:AAFQbaQNjtlhS2KCe9W_4-MxCR-2Wm9CKRc"
def mensaje(text):
    return message_handler(text, query.insetar_movimiento())
bot(TOKEN, mensaje)