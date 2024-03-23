# Diccionario
informacion_personal = {
'nombre':'Cristian Mora',
'edad':37,
'ciudad':'Quito',
'provincia':'Pichincha',
}
print(informacion_personal)

# Modificar el valor
informacion_personal['ciudad'] = 'Quito'
print(informacion_personal)

# Agregar nueva clave:valor
informacion_personal['profesion'] = 'Operador de cominicaciones Pluspetrol Ecuador'
print(informacion_personal)

# Verificar telefono y agregar
if 'telefono' in informacion_personal:
 print(informacion_personal['telefono'])
else:
 informacion_personal['telefono'] = '0964085964'
print(informacion_personal)

# Eliminar edad
informacion_personal.pop('edad')
print(informacion_personal)
