x = 10
if x > 50:
    print("Más grande que 50")
else:
    print("Más pequeño que 50")
#Valores booleanos : evalúa el valor de verdad de algo.
# Solo tiene dos valores: verdadero y falso (tenga en cuenta las mayúsculas T y F)
is_hungry = True
has_freckles = False

#Números : enteros (números enteros), números de coma flotante
# (comúnmente conocidos como números decimales) y números complejo
age = 35 # storing an int
weight = 160.57 # storing a float

#Cadenas - texto literal
name = "Joe Blue"

#Tuplas : un tipo de datos que es inmutable
# (no se puede modificar después de su creación)
# y puede contener un grupo de valores.
# Las tuplas pueden contener tipos de datos mixtos.

dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
#dog[1] = 'dachshund'# ERROR: cannot be modified ('tuple' object does not support item assignment)

#Listas : un tipo de datos que es mutable y puede contener un grupo de valores.
# Generalmente destinado a almacenar una colección de datos relacionados.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

#Diccionarios : un grupo de pares clave-valor.
# Los elementos del diccionario se indexan mediante claves únicas que se utilizan para acceder a los valores.
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}

#-- Funciones Comunes --
#Si alguna vez no estamos seguros del tipo de datos de un valor o variable,
# podemos usar la funcióntype para averiguarlo. Por ejemplo:
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

#Para los tipos de datos que tienen un atributo de longitud (por ejemplo, listas, diccionarios, tuplas, cadenas),
# podemos usar la lenfunción para obtener la longitud:
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11

#Conversión de tipo o conversión de tipo explícito
#print("Hello" + 42)			# output: TypeError
print("Hello " + str(42))		# output: Hello 42

total = 35
user_val = "26"
total = total + int(user_val)	# total will be 61
print(total)

#--- Declaraciones Condicionales ---

x = 12
if x > 50:
    print("mayor que 50")
else:
    print("menor que 50")
# porque x no es mayor que 50, la segunda instrucción de impresión es la única que se ejecutará

x = 55
if x > 10:
    print("mayor que 10")
elif x > 50:
    print("mayor que 50")
else:
    print("menor que 10")
# aunque x sea mayor que 10 y 50, la primera declaración verdadera es la única que se ejecutará, por lo que solo veremos 'mayor que 10'

if x < 10:
    print("menor que 10")
else:
    print("Es falsa")
# no sucede nada, porque la declaración es falsa

#si el incremento en el for es más de uno se debe especificar. Si el for comienza en 0 no es necesario indicarlo.
# for x in range(0, 10, 1):
# for x in range(0, 10):	# increment of +1 is implied
# for x in range(10):	# increment of +1 and start at 0 is implied

for x in range(0, 10, 2):
    print(x)
# salida: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# salida: 5, 2

#--- Para bucles a través de listas ---
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# salida: 0 abc, 1 123, 2 xyz

# OR

for v in my_list:
    print(v)
# salida: abc, 123, xyz

#--- Para bucles a través de diccionarios ---
#Los diccionarios también son iterables.
# Cuando iteramos a través de un diccionario, el iterador es cada una de las claves del diccionario.
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# salida: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# salida: Noelle, Python
#Los diccionarios también tienen algunos métodos adicionales que nos permiten
# iterar a través de ellos y tener las claves y / o valores como iterador.
#Pruebe estos para obtener una mejor comprensión:

# another way to iterate through the keys
for key in capitals.keys():
     print(key)
#to iterate through the values
for val in capitals.values():
     print(val)
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)


#-- While Loops --

for count in range(0,5):
    print("looping - ", count)

count = 0
while count < 5:
    print("looping - ", count)
    count += 1

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final de sentencia else")

for val in "string":
    if val == "i":
        break
    print(val)
# salida: s, t, r

for val in "string":
    if val == "i":
        continue
    print(val)
# salida: s, t, r, n, g
# Nota, no i en el output, pero el bucle continuo después de la ic

