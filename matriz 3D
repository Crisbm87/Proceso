# Definir los datos de temperatura diaria en varias ciudades
temperaturas = {
    'Ciudad De Quito': {
        'Lunes': [25, 24, 23, 25],
        'Martes': [26, 27, 25, 24],
        'Miércoles': [28, 27, 26, 26],
        'Jueves': [29, 28, 29, 30],
        'Viernes': [30, 31, 31, 32],
        'Sábado': [32, 33, 33, 34],
        'Domingo': [31, 31, 30, 29]
    },
    'Ciudad de Ibarra': {
        'Lunes': [22, 22, 23, 24],
        'Martes': [23, 24, 24, 25],
        'Miércoles': [25, 26, 26, 27],
        'Jueves': [27, 27, 28, 29],
        'Viernes': [29, 30, 30, 31],
        'Sábado': [30, 31, 32, 32],
        'Domingo': [29, 28, 28, 27]
    }

    
}

# Calcular el promedio de temperaturas para cada ciudad por semana
for ciudad, datos_semanales in temperaturas.items():
    print(f"Promedio de temperaturas para {ciudad}:")
    for dia_semana, temperaturas_dia in datos_semanales.items():
        promedio_semana = sum(temperaturas_dia) / len(temperaturas_dia)
        print(f"  {dia_semana}: {promedio_semana:.2f}")
