# Ejercicio #7 de funciones - Convertir grados Celsius a grados Fahrenheit.

# ZONA DE FUNCIONES.

def tomar_celsius():
    g_cels = int(input("Inserte los grados Celsius que desea convertir a Fahrenheit: "))
    return g_cels

def convertir_fahren(g_cels):
    fahren = (g_cels * (9 / 5)) + 32 
    return fahren

def imprimir_resultado(fahren):
    print("El número de grados Celsius que insertó, se traduce a", fahren, "grados Fahrenheit.")

# CÓDIGO PRINCIPAL.

g_cels = tomar_celsius() # Esta función la usamos para solicitarle los grados Celsius que el cliente desea convertir.

fahren = convertir_fahren(g_cels) # Esta función la usamos para convertir los grados Celsius a Fahrenheit.

imprimir_resultado(fahren) # Esta función la usamos para mostrarle el resultado al cliente en Fahrenheit. 