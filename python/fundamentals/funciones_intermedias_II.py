# 1.Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
# 2.Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
# 3.En el directorio sports_directory, cambia 'Messi' a 'Andres'
# 4.Camba el valor 20 en z a 30
        #0        #1
x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name': 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Cambio de datos en variables.

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0]= 'Andres'
z[0]['y'] = 30
print(z[0]['y'])
print(sports_directory['soccer'][0])

#Itera a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios,
#la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado.
# Por ejemplo, dada la siguiente lista:
students1 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students1):
    for x in students1:
        print('first_name -', x['first_name'], ', last_name -', x['last_name'])

iterateDictionary(students1)

#La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
#Bonus: Hacer que aparezcan exactamente así!
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#Obtén valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que,
#dada una lista de diccionarios y un nombre de clave,
#la función imprima el valor almacenado en esa clave para cada diccionario.
#Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:
def iterateDictionary2(students1):
    for x in students1:
        print(x['first_name'])

iterateDictionary2(students1)
print()
def iterateDictionary3(students1):
    for x in students1:
        print(x['last_name'])

iterateDictionary3(students1)

#Itera a través de un diccionario con valores de listas
#Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas
#imprima el nombre de cada clave junto con el tamaño de su lista
#y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print()

#print(dojo['locations'])
#print(dojo['instructors'])

print()

def printInfo(dojo):
    for info in dojo:
        print(len(dojo[info]), info, dojo[info])

printInfo(dojo)
