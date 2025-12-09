# Ejercicio #20 de funciones - Convertir litros a galones.

# ZONA DE FUNCIONES. 

def toma_litro():
    litros = float(input("Inserte la cantidad de litros que desea convertir a galones: "))
    return litros

def conv_galones(litros):
    galones = litros / 3.785
    return galones

def imprimir_rslt(galones):
    print("La cantidad de litros que insertó, se traduce a", galones, "galones.")

# CÓDIGO PRINCIPAL.

litros = toma_litro() # Esta función la uso para solicitar la cantidad de litros que el cliente desea convertir.

galones = conv_galones(litros) # Esta función la uso para realizar la conversión de litros a galones.

imprimir_rslt(galones) # Esta función la uso para mostrarle el resultado final al cliente (la conversión de litros a galones).