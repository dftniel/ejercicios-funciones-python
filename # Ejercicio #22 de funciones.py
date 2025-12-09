# Ejercicio #22 de funciones - Crea un algoritmo que pida al usuario dos números y calcule la resta del primero menos el segundo.

# ZONA DE FUNCIONES. 

def prim_num():
    onenum = int(input("Inserte un primer número: "))
    return onenum

def seg_num():
    secnum = int(input("Inserte un segundo número, que se le restará al primero que insertó: "))
    return secnum

def resta(onenum, secnum):
    resta_nums = onenum - secnum
    return resta_nums

def imprimir_resultado(resta_nums):
    print("La resta del primer número y el segundo da como resultado:", resta_nums)

# CÓDIGO PRINCIPAL 

onenum = prim_num() # Esta función la utilizo para pedir un primer número.

secnum = seg_num() # Esta función la utilizo para pedir el segundo número que se resta con el primero.

resta_nums = resta(onenum, secnum) # Esta función la utilizo para realizar la resta. 

imprimir_resultado(resta_nums) # Esta función la utilizo para mostrarle el resultado final al cliente.

