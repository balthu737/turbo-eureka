try:
    import telebot
    print("se importo de forma correcta")
except ModuleNotFoundError as e:
    print(e)
class Commnads():
    """
    Docstring for Commands
    En esta clase se van a guardar todos lo comandos del bot
    """
    def start(self):
        """
        Docstring for start
        Comando start, devuelve un inicio
        """
        return """
Hola! iniciaste balthu bot, este bot va a ser tu asistente personal.
Si quere saber como se usa toca aca --> /help
    """
    def help(self):
        """
        Docstring for help
        Comando help, enseña a usar el bot
        """
        return"""
Hola!
¿Como estas?

Esta es la forma de usar este bot:
gasto <monto> <categoria> 

Los comando que se pueden utilizar con este bot son los siguientes:
/categoria
    devuelve el total gastado en esa categoria.
/hoy
    devuelve el total gastado hoy y en que cateforias.
/semana
    devuelve el total gastado en la semana y en que cateforias.
/mes
    devuelve el total gastado en el mes y en que cateforias.
/anio
    devuelve el total gastado en el año y en que cateforias.
    """

    def categoria(self):
        """
        Docstring for categoria
        Comando categoria, devuelve las categorias excistente
        """
        return """
Hola estas son las categorias excistente
    """

    def hoy(self):
        """
        Docstring for hoy
        Comando hoy, devuelve los gastos del dia
        """
        return"""
Hola los gastos de hoy son
    """

    def semana(self):
        """
        Docstring for semana
        Comando semana, devuelve los gastos de la semana
        """
        return """
Hola los gastos de la semana son
    """

    def mes(self):
        """
        Docstring for mes
        Comando semana, devuelve los gastos del mes
        """
        return """
Hola los gastos del mes son
    """

    def anio(self):
        """
        Docstring for anio
        Comando semana, devuelve los gastos del año
        """
        return """
Hola los gastos del año son
    """


