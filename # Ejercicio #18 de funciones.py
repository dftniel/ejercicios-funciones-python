# Ejercicio #18 de funciones - Calcular el área de un hexágono regular con su lado dado.

# ZONA DE FUNCIONES. 

def toma_lado():
    lado = int(input("Inserte el lado del hexágono (centímetros): "))
    return lado

def calcular_perimetro(lado):
    perimetro = lado * 6
    return perimetro

def calcular_apotema(lado):
    apotema = (lado ** (1/3)) / 2 
    return apotema

def calcular_area(perimetro, apotema):
    area = (perimetro * apotema) / 2
    return area

def imprimir_rslt(area):
    print("El área del hexágono es:", area)

# CÓDIGO PRINCIPAL.

lado = toma_lado() # Esta función la usamos para solicitarle al cliente el lado del hexágono. 

perimetro = calcular_perimetro(lado) # Esta función la usamos para calcular el perimetro del hexágono.

apotema = calcular_apotema(lado) # Esta función la usamos para calcular el apotema del hexágono.

area = calcular_area(perimetro, apotema) # Esta función la uso para calcular el área del hexágono. 

imprimir_rslt (area) # Esta función la uso para mostrarle el resultado final al cliente. 