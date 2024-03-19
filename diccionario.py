# diccionario con información personal ficticia
informacion_personal = {
    "Nombre": "Cristian Benito Mora Cervantes",
    "Edad": 37,
    "Ciudad": "Quito",
    "Profesion": "Operador de comunicaciones - Pluspetrol Ecuador"
}

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregarla con un número de teléfono ficticio
    informacion_personal["Telefono"] = "0964085964"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Información personal:")
for key in informacion_personal:
    print(f"{key}: {informacion_personal[key]}")
