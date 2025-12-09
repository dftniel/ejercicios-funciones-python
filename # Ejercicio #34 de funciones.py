# Ejercicio #34 de funciones - Desarrolla un programa que pida el precio de un artículo y calcule el 10% de descuento. 

# ZONA DE FUNCIONES.

def toma_precio():
    precio = int(input("Por favor, inserte el precio del artículo: "))
    return precio

def cal_descuento(precio):
    desc = precio * 0.10
    return desc

def precio_f(desc, precio):
    precio_final = precio - desc
    return precio_final

def imprimir_rslt(precio_final):
    print("Con 10% de descuento, el precio del artículo es de:", precio_final)

# CÓDIGO PRINCIPAL. 

precio = toma_precio() # Con esta función tomo el precio original del artículo.

desc = cal_descuento(precio) # Con esta función realizo la operación para saber cuánto se le descontará al artículo.

precio_final = precio_f(desc, precio) # Con esta función se realiza la operación para saber cuál es el precio final del artículo.

imprimir_rslt(precio_final) # Con esta función doy el resultado, es decir, el precio final. 