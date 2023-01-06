#1. Crea dos arrays o arreglos unidimensionales que tengan el mismo tamaño 
# (lo pedirá por teclado), en uno de ellos almacenarás nombres de personas 
# como cadenas, en el otro array o arreglo ira almacenando la longitud de los nombres


lista = []
lista_tamanio = []
for i in range(3):
    x = input(str("Ingrese nombres: "))
    lista.append(x)
    y = len(x)
    lista_tamanio.append(y)
print(lista)
print(lista_tamanio)
