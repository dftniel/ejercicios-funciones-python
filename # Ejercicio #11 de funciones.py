# Ejercicio #11 de funciones - Convertir kilómetros a millas.

# ZONA DE FUNCIONES.

def obt_kilometros():
    kms = float(input("Inserte la cantidad de kilometros que desea convertir a millas: "))
    return kms

def calcular_mlls(kms):
    millas = kms / 1.609
    return millas

def imprimir_rslt(millas):
    print("La cantidad de kilometros que insertó se traduce a", millas, "millas.")

# CÓDIGO PRINCIPAL 

kms = obt_kilometros() # Esta función la uso para obtener los kilometros que el cliente desea convertir.

millas = calcular_mlls(kms) # Con esta función hago la conversión de km a millas.

imprimir_rslt(millas) # Con esta función muestro el resultado final al cliente (las millas).

