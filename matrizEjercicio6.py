#Calcular la determinante de una matriz.

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
        
#Hallar determinante
determinante = np.linalg.det(matrizA)
print(np.array(matrizA))
print(determinante)
