# Ejercicio #2 de funciones - Determinar el volumen de una esfera con su radio dado.

# ZONA DE FUNCIONES. 

def tomar_radio():
    radio = float(input("Por favor, inserte el radio de la esfera: "))
    return radio

def calcular_volumen(radio):
    volumen = (4 / 3) * (3.1416 * (radio ** 3))
    return volumen

def imprimir_resultado(volumen):
    print("El volumen de la esfera es:", volumen)

# CÓDIGO PRINCIPAL 

radio = tomar_radio() # Esta función la utilizamos para obtener el radio, dato que el cliente debe proporcionar.

volumen = calcular_volumen(radio) # Con esta función procesamos y hacemos el calculo del volumen de la esfera.

imprimir_resultado(volumen) # Con esta función mostramos el resultado al cliente, es decir, el volumen de la esfera.