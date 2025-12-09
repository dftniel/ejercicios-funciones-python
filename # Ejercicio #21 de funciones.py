# Ejercicio #21 de funciones - Escribe un programa que solicite dos números al usuario y muestre la suma de ambos. 

# ZONA DE FUNCIONES. 

def prim_num():
    onenum = int(input("Inserte un primer número: "))
    return onenum

def seg_num():
    secnum = int(input("Inserte el segundo número para sumarlo con el primero: "))
    return secnum

def sumanum(onenum, secnum):
    suma = onenum + secnum
    return suma

def imprimir_resultado(suma):
    print("La suma de ambos números es:", suma)

# CÓDIGO PRINCIPAL.

onenum = prim_num() # Esta función la utilizo para pedir el primer número.

secnum = seg_num() # Esta función la utilizo para pedir el segundo número, que se sumará con el primero.

suma = sumanum(onenum, secnum) # Esta función la utilizo para realizar la suma de ambos números.

imprimir_resultado(suma) # Esta función la utilizo para mostrar el resultado de la suma de los dos números. 