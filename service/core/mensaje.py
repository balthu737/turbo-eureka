def analisis(text, funcion):
    """
    Docstring for analisis
    
    :param text: Mensaje del usuario
    :param funcion: Funcion para añadir gastos
    """
    texto = text.lower().strip().split()
    if not texto:
        print("Formato inválido")
    if len(texto) < 3:
        print("Formato inválido: gasto <monto> <categoria>")
    if texto[0] != "gasto" or "ahorro":
        print("El comando debe empezar con 'gasto'")
    if not texto[1].isnumeric():
        print("El monto debe ser un número")
    monto = int(texto[1])
    categoria = texto[2]
    funcion(monto,categoria)
    print(f"Gasto registrado: {monto} en {categoria}")
