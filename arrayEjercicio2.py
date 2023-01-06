#Dada las siguientes notas almacenadas en un arreglo: [20,15,12,11,8,4,1]
#Elimine la nota más baja programáticamente sin usar la función (min) y escriba
#en pantalla. Luego programáticamente calcule el promedio de notas 
#descontando la nota eliminada.

A = [20, 15, 12, 11, 8, 4, 1]
maximo = 20
minimo = maximo 

for i in A:
    if i < minimo:
        minimo = i
print("El promedio más bajo es: ",minimo)
A.remove(minimo)
print(A)
suma = 0
for j in A:
    suma += j
print(suma)
print("El promedio de las notas es: ", suma/len(A))

