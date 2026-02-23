def analisis(usuario_id, text, funcion_gasto, funcion_ahorro):
    texto = text.lower().strip().split()
    if not texto:
        print("Formato inválido")
        return {"success": False, "mensaje": "Formato invalido."}
    if len(texto) < 2:
        print("⚠️ Formato inválido: gasto/ahorro <monto> [categoria]")
        return {"success": False, "mensaje": "⚠️ Formato inválido: gasto/ahorro <monto> [categoria]."}
    comando = texto[0]
    if comando not in ["gasto", "ahorro"]:
        print("El comando debe empezar con 'gasto' o 'ahorro'.")
        return {"success": False, "mensaje": "⚠️ El comando debe empezar con 'gasto' o 'ahorro'."}
    if not texto[1].isnumeric():
        print("❌ El monto debe ser un número")
        return {"success": False, "mensaje": "❌ El monto debe ser un número."}
    monto = int(texto[1])
    if comando == "gasto":
        if len(texto) < 3:
            print("⚠️ Formato inválido: gasto <monto> <categoria>")
            return {"success": False, "mensaje": "⚠️ Formato inválido: gasto <monto> <categoria>."}
        categoria = texto[2]
        funcion_gasto(usuario_id, monto, categoria)
        print(f"Gasto registrado: {monto} en {categoria}")
        return {"success": True, "mensaje": f'✅ Gasto registrado con exitos: {monto} en {categoria}.', "id": usuario_id}
    elif comando == "ahorro":
        funcion_ahorro(usuario_id, monto)
        print(f"Ahorro registrado: {monto}")
        return {"success": True, "mensaje": f'✅ Ahorro registrado con exito: {monto}.', "id": usuario_id}
    return {"success": False, "mensaje": "❌ No se reconoció el comando. Usa 'gasto' o 'ahorro'."}