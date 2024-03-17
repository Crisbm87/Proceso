def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad.

    :param datos_temperaturas: Un diccionario donde las claves son los nombres de las ciudades
                               y los valores son listas de listas con las temperaturas semanales.
    :return: Un diccionario con las ciudades y sus temperaturas promedio.
    """
    promedios = {}
    for ciudad, temperaturas in datos_temperaturas.items():
        # Aplanar la lista de listas de temperaturas y calcular el promedio
        temperaturas_aplanadas = [temp for semana in temperaturas for temp in semana]
        promedio_ciudad = sum(temperaturas_aplanadas) / len(temperaturas_aplanadas)
        promedios[ciudad] = promedio_ciudad
    return promedios

# Ejemplo de uso:
datos_ejemplo = {
    'QUITO': [[20, 21, 22], [23, 22, 21], [20, 19, 21], [22, 23, 24]],
    'CUENCA': [[30, 31, 32], [33, 32, 31], [30, 29, 31], [32, 33, 34]],
    'MANTA': [[10, 11, 12], [13, 12, 11], [10, 9, 11], [12, 13, 14]]
}

temperaturas_promedio = calcular_temperatura_promedio(datos_ejemplo)
print(temperaturas_promedio)
