# Ejercicio #32 de funciones - Diseña un algoritmo que calcule el área de un rectángulo, solicitando su longitud y ancho.

# ZONA DE FUNCIONES.

def tomar_longitud():
    longitud = int(input("Inserte la longitud del rectángulo (centímetros): "))
    return longitud

def tomar_ancho():
    ancho = int(input("Inserte el ancho del rectángulo (centímetros): "))
    return ancho

def calcular_area(longitud, ancho):
    area = longitud * ancho 
    return area

def imprimir_resultado(area):
    print("El área del rectángulo es:", area)

# CÓDIGO PRINCIPAL

longitud = tomar_longitud() # Esta función la uso para solicitar la longitud del rectángulo.

ancho = tomar_ancho() # Esta función la uso para solicitar el ancho del rectángulo. 

area = calcular_area(longitud, ancho) # Esta función la uso para realizar el cálculo del área del rectángulo.

imprimir_resultado(area) # Con esta función muestro el resultado de la operación. 
