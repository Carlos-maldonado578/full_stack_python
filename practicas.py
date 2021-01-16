#lista
#pares de elementos
#ordenadas segun su ingreso
#acepta todos los tipos de datos
#se pueden recorrer y modificar los valores
# conjunto de datos, ordenados según su ingreso, separados por coma (,), en []

lista_pares = [2,4,6,8,0]
print(lista_pares)#[2,4,6,8,0]
#todas comienzan en la posicion cero
print(lista_pares[0])#2
#acceder al ultimo elemento
print(lista_pares[len(lista_pares)-1])#0
print(lista_pares[-1])#0
#tamaño de una lista len(arreglo)
print(len(lista_pares))#5
#podemos recorrer el arreglo con valores negativos
print(lista_pares[-2])#8
print(lista_pares[-5])#2
print()
#arreglo vacio
arreglo = []
print("arreglo vacio Tamaño",len(arreglo))#0
print()
#secciones de lista [2,4,6,8,0]
print(lista_pares[3:])#[8,0]
print(lista_pares[:3])#[2,4,6]
print(lista_pares[1:])#[4, 6, 8, 0]
print(lista_pares[:4])#[2,4,6,8]
print(lista_pares[:])#todos los elementos
######
arreglo = lista_pares # igualando a la lista
arreglo2 = lista_pares[:]#obteniendo los valores del arreglo
print(arreglo)#[2, 4, 6, 8, 0]
#modificar un valor de la lista
lista_pares[2] = 5
print(lista_pares)#[2, 4, 5, 8, 0]
print(arreglo)#[2, 4, 5, 8, 0]
print(arreglo2)#no recibio cambio
num1 = lista_pares[2]
lista_pares[2] = 7
print(num1)
print(arreglo)#
print(arreglo2)#no recibio cambio
arreglo[0] =1
print(lista_pares)#[1, 4, 7, 8, 0]
arreglo.append("a")#agrega en la ultima posicion
print(arreglo)#




