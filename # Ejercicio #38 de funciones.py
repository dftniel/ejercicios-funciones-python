# Ejercicio #38 de funciones - Desarrolla un programa que pida dos números y muestre el mayor de los dos utilizando operadores aritméticos.

# ZONA DE FUNCIONES.

def prim_num():
    numeone = int(input("Inserte el primer número: "))
    return numeone

def seg_num():
    segnum = int(input("Inserte el segundo número: "))
    return segnum

def masmenos(numeone, segnum):
    if numeone > segnum:
        print("El primer número es mayor que el segundo.")
    else:
        print("El segundo número es mayor que el primero.")

def imprimir_rst():
    print("El programa finalizó.")

# CÓDIGO PRINCIPAL. 

numeone = prim_num() # Con esta función solicito el primer número.

segnum = seg_num() # Con esta función solicito el segundo número para llevar a cabo la operación.

masmenos(numeone, segnum) # Con esta función doy respuesta a lo que se me solicita.

imprimir_rst() # Con esta función muestro en pantalla que el programa finaliza. 