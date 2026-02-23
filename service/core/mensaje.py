def analisis(usuario_id, text, funcion_gasto, funcion_ahorro):
    texto = text.lower().strip().split()
    if not texto:
        print("Formato inválido")
        return
    if len(texto) < 2:
        print("Formato inválido: gasto/ahorro <monto> [categoria]")
        return
    comando = texto[0]
    if comando not in ["gasto", "ahorro"]:
        print("El comando debe empezar con 'gasto' o 'ahorro'")
        return
    if not texto[1].isnumeric():
        print("El monto debe ser un número")
        return
    monto = int(texto[1])
    if comando == "gasto":
        if len(texto) < 3:
            print("Formato inválido: gasto <monto> <categoria>")
            return
        categoria = texto[2]
        funcion_gasto(usuario_id, monto, categoria)
        print(f"Gasto registrado: {monto} en {categoria}")
    elif comando == "ahorro":
        funcion_ahorro(usuario_id, monto)
        print(f"Ahorro registrado: {monto}")
