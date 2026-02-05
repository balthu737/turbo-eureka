try:
    import telebot
    print("se importo de forma correcta")
except ModuleNotFoundError as e:
    print(e)
from bot.commands import Commnads

def bot(token, funcion):
    """
    Docstring for bot
    
    :param token: Token para identificar el bot
    :param funcion: Funcion que lee los mensajes
    """
    toke = token
    bot = telebot.TeleBot(toke)
    commands = Commnads()
    @bot.message_handler(commands=["start"])
    def start_handler(message):
        response = commands.start()
        bot.reply_to(message, response)
        print("Enviando comando /start...")
    @bot.message_handler(commands=["help"])
    def help_hamdler(message):
        responde = commands.help()
        bot.reply_to(message, responde)
        print("Enviando comando /help...")
    @bot.message_handler(commands=["categoria"])
    def categoria_handler(message):
        reponder = commands.categoria()
        bot.reply_to(message, reponder)
        print("Enviando comando /categoria...")
    @bot.message_handler(commands=["hoy"])
    def hoy_handler(message):
        reponder = commands.hoy()
        bot.reply_to(message, reponder)
        print("Enviando comando /hoy...")
    @bot.message_handler(commands=["semana"])
    def semana_handler(message):
        reponder = commands.semana()
        bot.reply_to(message, reponder)
        print("Enviando comando /semana...")
    @bot.message_handler(commands=["mes"])
    def mes_handler(message):
        reponder = commands.mes()
        bot.reply_to(message, reponder)
        print("Enviando comando /mes...")
    @bot.message_handler(commands=["anio"])
    def anio_handler(message):
        reponder = commands.anio()
        bot.reply_to(message, reponder)
        print("Enviando comando /año...")
    @bot.message_handler(func=lambda message: True)
    def guardar_mensaje(message):
        mensaje = message.text
        funcion(mensaje)
        print("Guardando mensaje...")
    bot.polling(non_stop=True)
    print("Escuchando...")

