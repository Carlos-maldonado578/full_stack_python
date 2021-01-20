#Cuenta regresiva : crea una función que acepte un número como entrada.
#Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número
#(como el elemento 0) hasta 0 (como el último elemento).
#Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]
def regret(num1):
    for x in range(num1, 0, -1):
        print(x)

regret(6)#no me entrega el cero



#Imprimir y volver : crea una función que recibirá una lista con dos números.
#Imprima el primer valor y devuelva el segundo.
#Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

def print_and_return(num1,num2):
    print(num1)
    return num2

print_and_return(1,2)

#First Plus Length : crea una función que acepta una lista
#y devuelve la suma del primer valor de la lista más la longitud de la lista.

lista= [1, 2, 3, 4, 5]
def largo(lista):
        print(lista[0] + len(lista))

largo(lista)

#Valores mayores que el segundo :
#escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original
#que sean mayores que su segundo valor.
#Imprima cuántos valores son y luego devuelva la nueva lista.
#Si la lista tiene menos de 2 elementos, haga que la función devuelva False
# Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# Ejemplo: values_greater_than_second ([3]) debería devolver False

list = [5, 2, 3, 2, 1, 4]
def mayor_segundo(list):
    if len(list) < 2:
        return False
    list1 = []
    for x in list:
        if x >= list[2]:
            list1.append(x)
    return list1

print(mayor_segundo(list))

#Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros:
# tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
#Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
#Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]

def long(a, b):
    for x in range(0, a, 1):
        print(b)

long(6, 2)
