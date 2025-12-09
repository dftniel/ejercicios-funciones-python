# Ejercicio #3 de funciones -  Calcular el área de un rectángulo con longitud y ancho dados.

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

longitud = tomar_longitud() # Esta función la utilizamos para obtener de parte del cliente la longitud del rectángulo.

ancho = tomar_ancho() # Esta función la utilizamos para obtener de parte del cliente el ancho del rectángulo.

area = calcular_area(longitud, ancho) # Esta función la utilizamos para calcular el área del rectángulo.

imprimir_resultado(area) # Con esta función le mostramos al cliente el área del rectángulos según los datos insertados. 

