# Ejercicio #35 de funciones - Diseña un algoritmo que solicite la cantidad de dinero en una cuenta y calcule el 5% de interés.

# ZONA DE FUNCIONES. 

def din_cuenta():
    dinero = float(input("Inserte la cantidad de dinero que hay en su cuenta: "))
    return dinero

def calc_interes(dinero):
    interes = dinero * 0.05
    return interes

def total(dinero, interes):
    tot = dinero + interes
    return tot

def imprimir_rslt(interes, tot):
    print("El interés de su cuenta es de:", interes)
    print("El total en la cuenta después de agregar el interés es de:", tot)

# CÓDIGO PRINCIPAL.

dinero = din_cuenta() # Con esta función solicito la cantidad de dinero en la cuenta.

interes = calc_interes(dinero) # Con esta función calculo el interés.

tot = total(dinero, interes) # Con esta función calculo el total (dinero + interés).

imprimir_rslt(interes, tot) # Con esta función muestro el resultado final. 
