# Ejercicio #33 de funciones - Crea un algoritmo que solicite una distancia en kilómetros y la convierta a millas. 

# ZONA DE FUNCIONES. 

def toma_kilometros():
    kilometros = float(input("Inserte la cantidad de kilometros que desea convertir a millas: "))
    return kms

def calcular_millas(kilometros):
    millas = kilometros / 1.609
    return millas

def imprimir_rslt(millas):
    print("La cantidad de kilometros que insertó se traduce a", millas, "millas.")

# CÓDIGO PRINCIPAL 

kilometros = toma_kilometros() # Con esta función solicito los kilometros 

millas = calcular_millas(kilometros) # Con esta función hago la conversión de km a millas.

imprimir_rslt(millas) # Con esta función muestro el resultado final al cliente (las millas).