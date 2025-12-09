# Ejercicio #30 de funciones - Crea un algoritmo que solicite el radio de un círculo y calcule su circunferencia. 

# ZONA DE FUNCIONES.

def toma_radio():
    radio = float(input("Inserte el radio del círculo: "))
    return radio

def calc_circ(radio):
    circunf = 2 * 3.1416 * radio
    return circunf

def imprimir_resultado(circunf):
    print("La circunferencia de el círculo es:", circunf)

# CÓDIGO PRINCIPAL.

radio = toma_radio() # Con esta función le solicito al cliente el radio del círculo.

circunf = calc_circ(radio) # Con esta función hallo la circunferencia del círculo.

imprimir_resultado(circunf) # Con esta función muestro el resultado final de la operación.

