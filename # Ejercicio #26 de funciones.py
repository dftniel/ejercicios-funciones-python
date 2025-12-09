# Ejercicio #26 de funciones - Crea un algoritmo que determine el residuo de la división entre dos números ingresados por el usuario.

def prim_num():
    onenum = int(input("Inserte un primer número: "))
    return onenum

def seg_num():
    secnum = int(input("Inserte un segundo número: "))
    return secnum

def residuo(onenum, secnum):
    resid_nums = onenum % secnum
    return resid_nums

def imprimir_resultado(resid_nums):
    print("El residuo entre ambos números da como resultado:", resid_nums)

# CÓDIGO PRINCIPAL 

onenum = prim_num() # Esta función la utilizo para pedir un primer número.

secnum = seg_num() # Esta función la utilizo para pedir el segundo número.

resid_nums = residuo(onenum, secnum) # Esta función la utilizo para realizar la operación de residuo. 

imprimir_resultado(resid_nums) # Esta función la utilizo para mostrarle el resultado final al cliente.
