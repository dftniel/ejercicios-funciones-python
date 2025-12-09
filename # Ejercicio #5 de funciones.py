# Ejercicio #5 de funciones - Calcular el área de un círculo con su radio dado.

# ZONA DE FUNCIONES. 

def obtener_radio():
    radio = float(input("Inserte el radio del círculo: "))
    return radio

def calcular_area(radio):
    area = 3.1416 * (radio ** 2)
    return area

def imprimir_resultado(area):
    print("El área del círculo es:", area)

# CÓDIGO PRINCIPAL 

radio = obtener_radio() # Esta función la usamos para obtener el radio del círculo, el cual es proporcionado por el cliente.

area = calcular_area(radio) # Con esta función calculamos el área del círculo.

imprimir_resultado(area) # Con esta función le mostramos el resultado final al cliente de la operación.