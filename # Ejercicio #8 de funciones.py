# Ejercicio #8 de funciones -  Convertir dólares a euros utilizando una tasa de cambio dada.

# ZONA DE FUNCIONES.

def tomar_tasacambio():
    dolar_cambio = float(input("Inserte el valor de un dólar en euros: "))
    return dolar_cambio

def tomar_conversion():
    dolares_cliente = float(input("¿Cuántos dólares desea convertir a euros?\n = "))
    return dolares_cliente

def conversion_dolareuro(dolar_cambio, dolares_cliente):
    euros_cliente = dolar_cambio * dolares_cliente
    return euros_cliente

def imprimir_resultado(euros_cliente):
    print("La cantidad de dólares que insertó, se traduce en", euros_cliente, "euros.")

# CÓDIGO PRINCIPAL.

dolar_cambio = tomar_tasacambio() # Esta función la usamos para solicitarle la tasa de cambio al cliente (a su elección).

dolares_cliente = tomar_conversion() # Esta función la usamos para solicitarle al cliente la cantidad de dólares que desea convertir a euros. 

euros_cliente = conversion_dolareuro(dolar_cambio, dolares_cliente) # Esta función es la que hace el cálculo de los dólares a euros.

imprimir_resultado(euros_cliente) # Esta función muestra el resultado final en euros de los dólares que el cliente inserta. 