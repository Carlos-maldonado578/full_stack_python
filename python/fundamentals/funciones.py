def add(a,b): # nombre de la función: 'add', parámetros: a y b
    x = a + b # proceso
    return x # retorno value: x
new_val = add(3, 5) # llamando a la función add, con los argumentos 3 y 5
print(new_val)    # el resultado de la función add se devuelve y se guarda en new_val, por lo que veremos 8

#Parámetros y Argumentos
def say_hi(name):
    print("Hi, " + name)

#invocando la función 3 veces, pasando un argumento cada vez;
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

#Valores devueltos

def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # el valor devuelto por la función se asigna a la variable
print(greeting) # mostrará 'Hi Michael'

def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
print(sum3)
