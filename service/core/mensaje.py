def analisis(usuario_id, text, funcion):
    texto = text.lower().strip().split()
    if not texto:
        print("Formato inválido")
        return
    if len(texto) < 3:
        print("Formato inválido: gasto <monto> <categoria>")
        return
    if texto[0] != "gasto":
        print("El comando debe empezar con 'gasto'")
        return
    if not texto[1].isnumeric():
        print("El monto debe ser un número")
        return
    monto = int(texto[1])
    categoria = texto[2]
    funcion(usuario_id, monto, categoria)
    print(f"Gasto registrado: {monto} en {categoria}")
