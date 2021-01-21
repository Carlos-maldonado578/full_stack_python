# 1. TAREA: imprimir "Hola mundo"
print("hola mundo")
# 2.imprimir "Hola Noelle!" con el nombre en una variable
name = "Noelle"
print( 'hola', name )	# con una coma
print( 'hola ' + name )	# con un +

# 3. imprimir "Hola 42!" con un numero en una variable
name = 42
print( 'Hola', name )	# con una coma
#print( 'Hola '+name )	# con un + - !Este debería darnos un error!

# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print('Me encanta comer {} y {}'.format(fave_food1,fave_food2)) # con .format()
print( f'Me encanta comer {fave_food1} y {fave_food2}' ) # con una cadena f

# python code below!
arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]

print(arr)
