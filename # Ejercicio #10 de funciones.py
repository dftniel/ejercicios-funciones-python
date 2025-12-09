# Ejercicio #10 de funciones - Determinar el volumen de un prisma rectangular con longitud, ancho y altura especificados. 

# ZONA DE FUNCIONES. 

def obt_longitud():
    longitud = int(input("Inserte la longitud del prisma rectangular (centímetros): "))
    return longitud

def obt_ancho():
    ancho = int(input("Inserte el ancho del prisma rectangular (centímetros): "))
    return ancho

def obt_altura():
    altura = int(input("Inserte la altura del prisma rectangular (centímetros): "))
    return altura

def calcular_volumen(longitud, ancho, altura):
    volumen = longitud * ancho * altura
    return volumen

def imprimir_resultado(volumen):
    print("El volumen del prisma rectangular es:", volumen)

# CÓDIGO PRINCIPAL. 

longitud = obt_longitud() # Esta función la usamos para solicitarle al cliente la longitud del prisma.

ancho = obt_ancho() # Esta función la usamos para solicitarle al cliente el ancho del prisma.

altura = obt_altura() # Esta función la usamos para solicitarle al cliente la altura del prisma.

volumen = calcular_volumen(longitud, ancho, altura) # Esta función la usamos para calcular el volumen del prisma.

imprimir_resultado(volumen) # Con esta función le mostramos el resultado (el volumen del prisma) al cliente. 
