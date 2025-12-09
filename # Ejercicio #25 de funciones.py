# Ejercicio #25 de funciones - Escribe un programa que solicite dos números y calcule la división del primero entre el segundo.

# ZONA DE FUNCIONES.

def prim_num():
    onenum = int(input("Inserte un primer número: "))
    return onenum

def seg_num():
    secnum = int(input("Inserte un segundo número, que se dividirá con el primero que insertó: "))
    return secnum

def divis(onenum, secnum):
    divis_nums = onenum / secnum
    return divis_nums

def imprimir_resultado(divis_nums):
    print("La división del primer número entre el segundo da como resultado:", divis_nums)

# CÓDIGO PRINCIPAL 

onenum = prim_num() # Esta función la utilizo para pedir un primer número.

secnum = seg_num() # Esta función la utilizo para pedir el segundo número que se dividiría con el primero.

divis_nums = divis(onenum, secnum) # Esta función la utilizo para realizar la división. 

imprimir_resultado(divis_nums) # Esta función la utilizo para mostrarle el resultado final al cliente.