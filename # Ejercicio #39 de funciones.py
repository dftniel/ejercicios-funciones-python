# Ejercicio #39 de funciones - Diseña un algoritmo que solicite dos números y calcule el promedio de ambos. 

# ZONA DE FUNCIONES. 

def prim_num():
    numeone = int(input("Inserte el primer número: "))
    return numeone

def seg_num():
    segnum = int(input("Inserte el segundo número: "))
    return segnum

def calc_prom(numeone, segnum):
    promedio = (numeone + segnum) / 2
    return promedio 

def imprimir_resultado(promedio):
    print("El promedio de ambos números es de:", promedio)

# CÓDIGO PRINCIPAL. 

numeone = prim_num() # Con esta función solicito el primer número. 

segnum = seg_num() # Con esta función solicito el segundo número para llevar a cabo la operación.

promedio = calc_prom(numeone, segnum) # Con esta función realizo la operación para hallar el promedio.

imprimir_resultado(promedio) # Con esta función doy el resultado a la operación. 

