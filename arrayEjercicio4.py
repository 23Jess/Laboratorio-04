#Diseñe un programa que lea un vector y calcule si hay un número que
#sea igual a la suma de los demás elementos del vetor.

import numpy as np
numeros=[]
i=1
while i !=0:
    i=int(input("Ingrese un numero: "))
    if i !=0:
        numeros.append(i)

suma = 0
for i in numeros:
    suma = suma + i

print(f"La suma acumulada es; {suma}")