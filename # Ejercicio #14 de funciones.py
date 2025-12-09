# Ejercicio #14 de funciones - Convertir pulgadas a centímetros.

# ZONA DE FUNCIONES. 

def toma_pulgadas():
    pulgadas = float(input("Inserte la cantidad de pulgadas que desea convertir a centímetros: "))
    return pulgadas

def conv_cms(pulgadas):
    cms = pulgadas * 2.64
    return cms

def imprimir_rslt(cms):
    print("La cantidad de pulgadas que insertó, se traducen a", cms, "centímetros.")

# CÓDIGO PRINCIPAL 

pulgadas = toma_pulgadas() # Esta función la uso para solicitarle al cliente las pulgadas que desea convertir.

cms = conv_cms(pulgadas) # Esta función se usa para realizar la conversión a centímetros.

imprimir_rslt(cms) # Esta función la uso para mostrarle el resultado final al cliente (los centímetros).

