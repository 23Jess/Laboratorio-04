#Suma, resta, multiplicación de matrices.

#Suma
import numpy as np
A = np.array([[1,2,3,4,5],[6,7,8,9,0]])
B = np.array([[3,2,0,4,3],[0,2,1,7,4]])

sumaMatrices = A + B
print(A)
print(B)
print("La suma de matrices es:\n", sumaMatrices)

#Resta
A = np.array([[1,2,3,4,5],[6,7,8,9,0]])
B = np.array([[3,2,0,4,3],[0,2,1,7,4]])

restaMatrices = A - B
print(A)
print(B)
print("La resta de matrices es:\n", restaMatrices)

#Multiplicación
A = np.array([[1,2,3,4],[6,7,8,9]])
B = np.array([[3,2,0,4],[0,2,1,7]])

multiplicacionMatrices = A * B
print(A)
print(B)
print("La multiplicación de matrices es:\n", multiplicacionMatrices)