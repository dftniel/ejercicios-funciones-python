# Ejercicio #1 de funciones -  Calcular el área de un triángulo con base y altura dadas.

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

base = tomar_base() # Esta función la uso para obtener la base del triángulo, que debe ser ingresada por el cliente.

altura = tomar_altura() # Esta función la uso para obtener la altura del triángulo, que debe ser ingresada por el cliente.

area = calcular_area(base, altura) # Con esta función calculamos el área del triángulo.

imprimir_resultado(area) # Con esta función le damos el resultado al cliente de cuál es el área del triángulo.

