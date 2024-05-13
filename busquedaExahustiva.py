def busqueda_exhaustiva(posicion_inicial, desplazamiento_maximo, funcion_prueba):
    for desplazamiento in range(-desplazamiento_maximo, desplazamiento_maximo + 1):
        posicion_actual = posicion_inicial + desplazamiento
        if funcion_prueba(posicion_actual):
            return posicion_actual
    return None  # Si no se encuentra la posición adecuada

# Función de prueba simulada
def es_posicion_correcta(posicion):
    # Simula la verificación del robot
    posicion_objetivo = 5  # Supongamos que la posición correcta es 5
    return posicion == posicion_objetivo

# Uso del algoritmo
posicion_inicial = 0
desplazamiento_maximo = 10
resultado = busqueda_exhaustiva(posicion_inicial, desplazamiento_maximo, es_posicion_correcta)
print("Posición encontrada:", resultado if resultado is not None else "No encontrada")
