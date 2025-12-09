# Ejercicio #4  de funciones - Determinar el volumen de un cilindro con radio de la base y altura especificados. 

# ZONA DE FUNCIONES.

def tomar_radio_base():
    radio_base = float(input("Inserte el radio de la base del cilindro: "))
    return radio_base

def tomar_altura():
    altura = int(input("Inserte la altura del cilindro: "))
    return altura

def calcular_volumen(radio_base, altura):
    volumen = 3.1416 * (radio_base ** 2) * altura
    return volumen

def imprimir_resultado(volumen):
    print("El volumen del cilindro es de:", volumen)

# CÓDIGO PRINCIPAL.

radio_base = tomar_radio_base() # Esta función la utilizamos para solicitarle al cliente el radio del cilindro.

altura = tomar_altura() # Esta función la utilizamos para solicitarle al cliente la altura del cilindro.

volumen = calcular_volumen(radio_base, altura) # Con esta función calculamos el volumen del cilindro.

imprimir_resultado(volumen) # Con esta función le damos el resultado al cliente de la operación.