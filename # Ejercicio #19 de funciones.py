# Ejercicio #19 de funciones - Determinar el volumen de un prisma triangular con la longitud de la base, altura y ancho especificados.

# ZONA DE FUNCIONES. 

def long_base():
    longitud = int(input("Inserte la longitud de la base del prisma triangular (centímetros): "))
    return longitud

def altura_pris():
    altura = int(input("Inserte la altura del prisma triangular (centímetros): "))
    return altura

def altura_triang():
    alturat = int(input("Inserte la altura del triángulo (centímetros): "))
    return alturat

def calc_volumen(longitud, altura, alturat):
    volumen = (longitud * altura * alturat) / 2
    return volumen

def imprimir_rslt(volumen):
    print("El volumen del prisma triangular es:", volumen)

# CÓDIGO PRINCIPAL.

longitud = long_base() # Esta función la uso para solicitar la longitud de la base.

altura = altura_pris() # Esta función la uso para solicitar la altura del prisma triangular.

alturat = altura_triang() # Esta función la uso para solicitar la altura del triángulo.

volumen = calc_volumen(longitud, altura, alturat) # Esta función la uso para calcular el volumen del prisma triangular.

imprimir_rslt(volumen) # Esta función la uso para mostrarle el resultado final al cliente (el volumen del prisma).



