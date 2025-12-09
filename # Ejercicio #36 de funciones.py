# Ejercicio #36 de funciones - Escribe un programa que pida dos números enteros y muestre el cociente de la división entera.

# ZONA DE FUNCIONES. 

def prim_num():
    numeone = int(input("Inserte el primer número: "))
    return numeone

def seg_num():
    segnum = int(input("Inserte el segundo número: "))
    return segnum

def cal_coc(numeone, segnum):
    cociente = numeone // segnum
    return cociente

def imprimir_rslt(cociente):
    print("El cociente de la división es:", cociente)

# CÓDIGO PRINCIPAL.

numeone = prim_num() # Con esta función solicito el primer número.

segnum = seg_num() # Con esta función solicito el segundo número para llevar a cabo la operación.

cociente = cal_coc(numeone, segnum) # Con esta función realizo la operación.

imprimir_rslt(cociente) # Con esta función muestro el resultado de la operación. 

