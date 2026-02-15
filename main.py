from bot.telegram_bot import bot
from database.query import Querys
from service.core.mensaje import analisis
from service.core.service import Gasto, Usuarios

TOKEN = "8017156472:AAFQbaQNjtlhS2KCe9W_4-MxCR-2Wm9CKRc"
def mensaje(text):
    return analisis(text)
bot(TOKEN, mensaje)
