# Ejercicio #16 de funciones - Determinar el volumen de un cubo con la longitud de un lado especificada. 

# ZONA DE FUNCIONES.

def long_lado():
    lado = int(input("Inserte la longitud del lado (centímetros): "))
    return lado

def calcular_volumen():
    volumen = lado ** 3
    return volumen

def imprimir_rslt(volumen):
    print("El volumen del cubo es:", volumen)

# CÓDIGO PRINCIPAL.

lado = long_lado() # Esta función la uso para solicitarle al cliente la longitud del lado del cubo.

volumen = calcular_volumen() # Esta función la uso para calcular el volumen del cubo.

imprimir_rslt(volumen) # Esta función la uso para mostrarle el resultado final al cliente. 
