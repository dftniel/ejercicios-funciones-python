# Ejercicio #17 de funciones - Convertir libras a kilogramos.

# ZONA DE FUNCIONES. 

def toma_libras():
    libras = float(input("Inserte la cantidad de libras que desea convertir a kilogramos: "))
    return libras

def convertir_kg(libras):
    kgs = libras / 2.205
    return kgs

def imprimir_rslt(kgs):
    print("La cantidad de libras que insertó, se traducen en", kgs, "kilogramos.")

# CÓDIGO PRINCIPAL.

libras = toma_libras() # Esta función la uso para solicitarle al cliente la cantidad de libras que desea convertir a kilogramos.

kgs = convertir_kg(libras) # Esta función la uso para realizar la conversión de libras a kilogramos.

imprimir_rslt(kgs) # Esta función la uso para mostrarle el resultado final al cliente. 

