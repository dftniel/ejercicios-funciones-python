# Ejercicio #37 de funciones - Crea un algoritmo que determine si un número es múltiplo de otro ingresados por el usuario.

# ZONA DE FUNCIONES. 

def prim_num():
    numeone = int(input("Inserte el primer número: "))
    return numeone

def seg_num():
    segnum = int(input("Inserte el segundo número: "))
    return segnum

def multip(numeone, segnum):
    if numeone % segnum == 0:
        print("El primer número es múltiplo del segundo.\n")
    else: 
        print("El primer número no es múltiplo del segundo.\n")

def imprimir_rslt():
    print("El programa finalizó.")

# CÓDIGO PRINCIPAL.

numeone = prim_num() # Con esta función solicito el primer número.

segnum = seg_num() # Con esta función solicito el segundo número para llevar a cabo la operación.

multip(numeone, segnum) # Con esta función doy respuesta a lo que se solicita.

imprimir_rslt() # Con esta función doy el programa por finalizado.
