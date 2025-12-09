# Ejercicio #15 de funciones - Calcular el área de un paralelogramo con base y altura dadas.

# ZONA DE FUNCIONES. 

def toma_base():
    base = int(input("Inserte la base del paralelogramo (centímetros): "))
    return base

def toma_altura():
    altura = int(input("Inserte la altura del paralelogramo (centímetros): "))
    return altura

def calcular_area(base, altura):
    area = base * altura
    return area

def imprimir_rslt(area):
    print("El área del paralelogramo es:", area)

# CÓDIGO PRINCIPAL.

base = toma_base() # Esta función la uso para solicitarle al cliente la base del paralelogramo.

altura = toma_altura() # Esta función la uso para solicitarle al cliente la altura del paralelogramo.

area = calcular_area(base, altura) # Esta función la uso para calcular el área del paralelogramo.

imprimir_rslt(area) # Esta función la uso para mostrarle el resultado final al cliente (el área del paralelogramo).