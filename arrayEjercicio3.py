#Crea un array o arreglo unidimensional donde le indiques el tamaño por teclado
#y crear una función que rellene el array o arreglo con los múltiplos
#de un número pedido por teclado. Por ejemplo, si defino un array de tamaño 5 y elijo un
#3 en la función, el array contendrá 3, 6, 9, 12, 15. Muéstralos por pantalla
#usando otra función distinta.

A = int(input("Ingrese el tamaño del array: "))
B = int(input("Ingrese el número de múltiplos: "))

C = []
for i in range (0,A):
    C.append(i*B)
print (C)