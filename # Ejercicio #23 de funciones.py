# Ejercicio #23 de funciones - Desarrolla un programa que requiera dos números y muestre el producto de dichos valores.

# ZONA DE FUNCIONES. 

def prim_num():
    onenum = int(input("Inserte un primer número: "))
    return onenum

def seg_num():
    secnum = int(input("Inserte un segundo número, que se multiplicará con el primero que insertó: "))
    return secnum

def multip(onenum, secnum):
    multip_nums = onenum * secnum
    return multip_nums

def imprimir_resultado(multip_nums):
    print("La multiplicación del primer número con el segundo da como resultado:", multip_nums)

# CÓDIGO PRINCIPAL 

onenum = prim_num() # Esta función la utilizo para pedir un primer número.

secnum = seg_num() # Esta función la utilizo para pedir el segundo número que se multiplica con el primero.

multip_nums = multip(onenum, secnum) # Esta función la utilizo para realizar la multiplicación. 

imprimir_resultado(multip_nums) # Esta función la utilizo para mostrarle el resultado final al cliente.