#Calcular la diagonal principal de una matriz

import numpy as np 

print("Ingrese el orden de la matriz a calcular: ")
filasA, columnasA = int(input()), int(input())

diagonal = 0

if filasA == columnasA:
    #creando la matriz vacia
    matrizA = []
    for i in range (filasA):
        matrizA.append([0]*columnasA)
    #rellenando la matriz
    print("Ingrese la matriz A ")
    for fila in range(filasA):
        for columna in range(columnasA):
            matrizA[fila][columna] = float(input(f"Ingrese la posición número {fila}, {columna}: "))
    #calculando la matriz diagonal principal de la matriz A
    for fila in range(filasA):
        for columna in range(columnasA):
            if fila == columna:
                diagonal += matrizA[fila][columna]
    
    print(np.array(matrizA))
    print(f"El valor de la diagonal principal es: {diagonal} ")
