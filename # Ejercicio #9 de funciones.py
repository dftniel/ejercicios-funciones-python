# Ejercicio #9 de funciones - Calcular el área de un trapecio con sus longitudes de bases y altura especificadas. 

# ZONA DE FUNCIONES. 

def obt_basemenor(): 
    basemenor = int(input("Inserte la base menor del trapecio (centímetros): "))
    return basemenor

def obt_basemayor():
    basemayor = int(input("Inserte la base mayor del trapecio (centímetros): "))
    return basemayor

def obt_altura():
    altura = int(input("Inserte la altura del trapecio (centímetros): "))
    return altura

def calcular_area(basemenor, basemayor, altura):
    area = ((basemenor + basemayor) * altura) / 2
    return area

def imprimir_resultado(area):
    print("El área del trapecio es: ", area)

# CÓDIGO PRINCIPAL. 

basemenor = obt_basemenor() # Con esta función, obtenemos la base menor del trapecio (el cliente la provee).

basemayor = obt_basemayor() # Con esta función, obtenemos la base mayor del trapecio (el cliente la provee).

altura = obt_altura() # Con esta función, obtenemos la altura del trapecio (el cliente la provee).

area = calcular_area(basemenor, basemayor, altura) # Con esta función, calculamos el área del trapecio.

imprimir_resultado(area) # Con esta función, le mostramos el resultado final (el área del trapecio) al cliente. 