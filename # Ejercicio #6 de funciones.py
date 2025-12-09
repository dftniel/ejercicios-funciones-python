# Ejercicio #6 de funciones - Determinar el volumen de un cono con radio de la base y altura especificados. 

# ZONA DE FUNCIONES.

def tomar_radio_base():
    radio_base = float(input("Inserte el radio del cono: "))
    return radio_base

def tomar_altura(): 
    altura = int(input("Inserte la altura del cono (centímetros): "))
    return altura

def calcular_volumen(radio_base, altura):
    volumen = (1 / 3) * (3.1416) * (radio_base ** 2) * altura
    return volumen

def imprimir_resultado(volumen):
    print("El volumen del cono es:", volumen)

# CÓDIGO PRINCIPAL 

radio_base = tomar_radio_base() # Con esta función le solicitamos al cliente el radio del cono.

altura = tomar_altura() # Con esta función le solicitamos al cliente la altura del cono.

volumen = calcular_volumen(radio_base, altura) # Con esta función calculamos el volumen del cono.

imprimir_resultado(volumen) # Con esta función le mostramos el resultado final al cliente. 