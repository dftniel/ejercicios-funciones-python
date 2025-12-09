# Ejercicio #29 de funciones - Escribe un programa que pida un número y determine si es par o impar usando el operador de módulo (%).

# ZONA DE FUNCIONES.

def numero():
    num = int(input("Inserte un número para saber si par o impar: "))
    return num

def par_imp(num):
    if num % 2 == 0:
        print("El número es par.\n")
    else:
        print("El número es impar.\n")

def imprimir_resultado():
    print("El programa finalizó.")

# CÓDIGO PRINCIPAL.

num = numero() # Con esta función solicito el número al cliente, para saber si es par o impar.

par_imp(num) # Con esta función determino si el número es par o impar.

imprimir_resultado() # Con esto le muestro al cliente que el programa finaliza. 