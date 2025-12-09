# Ejercicio #24 de funciones - Diseña un algoritmo que pida un número y calcule su cuadrado utilizando el operador de multiplicación.

# ZONA DE FUNCIONES. 

def numero():
    num = int(input("Inserte un número para averiguar su cuadrado: "))
    return num

def cuad_num(num):
    cuadrado = num ** 2
    return cuadrado

def imprimir_resultado(cuadrado):
    print("El cuadrado del número que insertó es:", cuadrado)

# CÓDIGO PRINCIPAL 

num = numero() # Con esta función le solicito al cliente el número que se elevará al cuadrado.

cuadrado = cuad_num(num) # Con esta función elevo el número al cuadrado.

imprimir_resultado(cuadrado) # Con esta función muestro el resultado de la operación al cliente.

