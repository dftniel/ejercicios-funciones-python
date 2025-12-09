# Ejercicio #31 de funciones - Desarrolla un programa que pida un número de horas y lo convierta a minutos utilizando operadores aritméticos.

# ZONA DE FUNCIONES.

def toma_hora():
    horas = int(input("Inserte el número de horas que quiere convertir a minutos: "))
    return horas

def calc_mins(horas):
    mins = horas * 60
    return mins

def imprimir_rslt(mins):
    print("Las cantidad de horas que introdujo, se traducen a:", mins, "minutos.")

# CÓDIGO PRINCIPAL.

horas = toma_hora() # Con esta función solicito la cantidad de horas.

mins = calc_mins(horas) # Con esta función convierto las horas a minutos.

imprimir_rslt(mins) # Con esta función muestro el resultado de la operación.

