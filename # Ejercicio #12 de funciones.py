# Ejercicio #12 de funciones - Calcular el área de un cuadrado con el lado dado.

# ZONA DE FUNCIONES. 

def toma_lado():
    lado = int(input("Inserte el lado del cuadrado (centímetros): "))
    return lado

def calcular_area(lado):
    area = lado ** 2
    return area

def imprimir_rslt(area):
    print("El area del cuadrado es:", area)

# CÓDIGO PRINCIPAL 

lado = toma_lado() # Esta función la uso para solicitarle al cliente el lado del cuadrado.

area = calcular_area(lado) # Esta función la uso para calcular el área del cuadrado.

imprimir_rslt(area) # Con esta función doy el resultado final al cliente (el área del cuadrado).