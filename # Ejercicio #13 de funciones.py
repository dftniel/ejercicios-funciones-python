# Ejercicio #13 de funciones - Determinar el volumen de una pirámide con longitud de la base, ancho de la base y altura especificados. 

# ZONA DE FUNCIONES.

def long_base():
    long = int(input("Inserte la longitud de la base de la pirámide (centímetros): "))
    return long

def ancho_base():
    ancho = int(input("Inserte el ancho de la base de la pirámide (centímetros): "))
    return ancho

def altura_pir():
    altura = int(input("Inserte la altura de la pirámide (centímetros): "))
    return altura

def calcular_area_base(long, ancho):
    area_base = long * ancho 
    return area_base

def calcular_vol(area_base, altura):
    volumen = (1 / 3) * (area_base * altura)
    return volumen

def imprimir_rslt(volumen):
    print("El volumen de la pirámide es:", volumen)

# CÓDIGO PRINCIPAL.
 
long = long_base() # Esta función la uso para solicitar la longitud de la pirámide.

ancho = ancho_base() # Esta función la uso para solicitar el ancho de la pirámide.

altura = altura_pir() # Esta función la uso para solicitar la altura de la pirámide. 

area_base = calcular_area_base(long, ancho) # Esta función la uso para calcular el área de la base de la pirámide. 

volumen = calcular_vol(area_base, altura) # Esta función la uso para calcular finalmente el volumen de la pirámide.

imprimir_rslt(volumen) # Esta función la uso para mostrarle el resultado final al cliente. 