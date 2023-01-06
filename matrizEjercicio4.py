#Hallar la matriz transpuesta

A= int(input("Digite el número de filas: "))
B=int(input("Digite el número de columnas: "))

M=[0]*A
for i in range(0,A):
    M[i]=[0]*B

matrizTranspuesta=[0]*B
for i in range(0,B):
    matrizTranspuesta[i]=[0]*A

#llenar la matriz M
for f in range(0,A):
    for c in range(0,B):
        M[f][c]=int(input("Digite el valor de M: "))

#llenar la matriz transpuesta sobre M
for f in range(0,A):
    for c in range(0,B):
        matrizTranspuesta[c][f]=M[f][c]

#imprime la matriz M
for f in range(0,A):
    for c in range(0,B):
        print(M[f][c], ",", end="")
    print()
print()
#imprime matriz transpuesta
for f in range(0,A):
    for c in range(0,B):
        print(matrizTranspuesta[f][c], ",", end="")
    print()
