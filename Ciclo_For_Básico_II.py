#Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
#Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]
#mayor a >
#menor a <
list= [- 1, 3, 5, -5]

def biggie_size(list):
    for x in range(len(list)):
        if list[x] > 0:
            list[x] = "big"
    return list

print(biggie_size(list))

#Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos.
#(Tenga en cuenta que cero no se considera un número positivo).
#Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
#Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve
list1 = [1,6, -4, -2, -7, -2]
def contar_pos(list1):
    contar = 0
    for x in range(len(list1)):
        if list1[x] > 0:
            contar = contar + 1
    list1[len(list1)-1] = contar
    return list1

print(contar_pos(list1))
#Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
#Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#Ejemplo: sum_total ([6,3, -2]) debería devolver 7
lista = [6,3, -2]
def sum_total(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]
    return suma
print(sum_total(lista))

#Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
lista = [1,2,3,4]
def promedio(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]
    promedio = suma / len(lista)
    return promedio
print(promedio(lista))

#Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
#Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
#Ejemplo: longitud ([]) debería devolver 0

lista = [37,2,1, -9]
def long(lista):
    return len(lista)

print(long(lista))

#Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista.
# Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#Ejemplo: mínimo ([]) debería devolver False
lista = [37,2,1, -9]
def minimo(lista):
    if len(lista) < 1:
        return False
    lista2 = []
    min = lista[0]
    for x in range(len(lista)):
        if min > lista[x]:
            min = lista[x]
    lista2.append(min)
    return lista2
print(minimo(lista))

#Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz.
# Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
#Ejemplo: máximo ([]) debería devolver False
lista = [37,2,1, -9]
def maximo(lista):
    if len(lista) < 1:
        return False
    lista2 = []
    max = lista[0]
    for x in range(len(lista)):
        if max < lista[x]:
            max = lista[x]
    lista2.append(max)
    return lista2
print(maximo(lista))

#Análisis final : crea una función que tome una lista y devuelva un diccionario
#que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
#Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver
# {'totalTotal': 31, 'promedio': 7.75, 'mínimo': -9, 'máximo': 37, 'longitud': 4}
lista = [37, 2, 1, -9]
def SPMML(lista):
    analisis = dict()
    present = ["totalTotal", "promedio", "minimo", "maximo", "longitud"]
    lista2 = []
    maximo = lista[0]
    minimo = lista[0]
    promedio = lista[0]
    suma = 0
    for x in range(len(lista)):
        if maximo < lista[x]:
            maximo = lista[x]
        elif minimo > lista[x]:
            minimo = lista[x]
        suma = suma + lista[x]
        promedio = suma / len(lista)
    lista2.append(suma)
    lista2.append(promedio)
    lista2.append(minimo)
    lista2.append(maximo)
    lista2.append(len(lista))
    for i in range(len(present)):
        analisis[present[i]] = lista2[i]
    return analisis
print(SPMML(lista))

#Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos.
#Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
list=[37,2,1, -9]
list.reverse()
print(list)