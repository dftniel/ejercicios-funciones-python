# Ejercicio #27 de funciones - Desarrolla un programa que pida un número y calcule su raíz cuadrada utilizando operadores aritméticos.

# ZONA DE FUNCIONES. 

def numero():
    num = int(input("Inserte un número, para averiguar su raíz cuadrada: "))
    return num

def raiz_cuad(num):
    raiz = num ** (1/2)
    return raiz

def imprimir_rslt(raiz):
    print("La raíz cuadrada del número que insertó es:", raiz)

# CÓDIGO PRINCIPAL

num = numero() # Esta función la utilizo para solicitar el número el cual se desea saber su raíz cuadrada.

raiz = raiz_cuad(num) # Esta función la utilizo para realizar la operación.

imprimir_rslt(raiz) # Esta función la utilizo para mostrar el resultado al cliente. 