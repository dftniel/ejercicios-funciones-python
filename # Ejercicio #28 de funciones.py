# Ejercicio #28 de funciones - Diseña un algoritmo que solicite la base y la altura de un triángulo y calcule su área.

# ZONA DE FUNCIONES. 

def tomar_base():
    base = int(input("Digite la base del triángulo: "))
    return base

def tomar_altura():
    altura = int(input("Digite la altura del triángulo: "))
    return altura

def calcular_area(base, altura):
    area = (base * altura) / 2 
    return area

def imprimir_resultado(area):
    print("El área del triángulo es:", area)

# CÓDIGO PRINCIPAL.

base = tomar_base() # Con esta función solicito la base del triángulo.

altura = tomar_altura() # Con esta función solicito la altura del triángulo.

area = calcular_area(base, altura) # Con esta función se calcula el área del triángulo.

imprimir_resultado(area) # Con esta función le muestro el resultado al cliente de la operación. 
