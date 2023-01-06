#Hallar la matriz simétrica
import numpy as np

print("Ingrese el orden de la matriz a calcular: ")
filasA, columnasA = int(input()), int(input())

contador = 0

if columnasA == filasA:
    #creando la matriz vacia
    matrizA = []
    for i in range (filasA):
        matrizA.append([0]*columnasA)
    #rellenando la matriz
    print("Ingrese la matriz A ")
    for fila in range(filasA):
        for columna in range(columnasA):
            matrizA[fila][columna] = float(input(f"Ingrese la posición número {fila}, {columna}: "))

    #Calculando si una matriz es simétrica o no
    for fila in range(filasA):
        for columna in range(columnasA):
            normal=matrizA[fila][columna]
            transpuesta=matrizA[columna][fila]
            if normal == transpuesta:
                contador += 1
    print(np.array(matrizA))

    
    if contador ==(filasA*columnasA):
        print("La matriz SÍ es simétrica")
    else:
        print("La matriz NO es simétrica")
else:
    print("La matriz no es simétrica")

