# Objetivos:
# Familiarícese con las listas de corte y las tuplas.
# Aprende algunos métodos de secuencia incorporados
# ¿Qué son las secuencias?
# Las secuencias son cualquier cosa sobre la que podamos iterar secuencialmente, incluidas listas, tuplas y cadenas.
# Aquí aprenderemos algunas cosas interesantes que podemos hacer con instancias de estas clases.
#
# Rebanar
# Si estamos interesados en obtener subconjuntos de valores de una secuencia, Python proporciona una forma de segmentar [:].
# Indicamos el índice inicial a la izquierda y el índice final (exclusivo) a la derecha.
# Si no indicamos un valor a la izquierda, comenzará en el índice 0; Si no se especifica el valor de la derecha, asumirá la longitud de la secuencia.
# Al igual que el método de división en JavaScript, la utilización de esta sintaxis devuelve una copia del tipo de datos con los valores especificados.
my_list = [99,4,2,5,-3]
my_tuple = (99,4,2,5,-3)
my_str = "sequoia"
print(my_list[:])
# output: [99,4,2,5,-3]
print(my_tuple[1:])
# output: (4,2,5,-3)
print(my_str[:3])
# output: "seq"
print(my_tuple[2:4])
# output: (2,5)
print(my_list, my_tuple, my_str)
# output: [99,4,2,5,-3] (99,4,2,5,-3) 'sequoia' -- note the original values have not changed

#Otros métodos de secuencia incorporados
# Aquí hay algunas funciones incorporadas de uso común para secuencias:
#
# max(sequence) devuelve el valor más grande en la secuencia
# sum(sequence) devuelve la suma de todos los valores en secuencia
# map(function, sequence) aplica la función a cada elemento en la secuencia que pasa. Devuelve una lista de los resultados.
# min(sequence) devuelve el valor más bajo en una secuencia.
# sorted(sequence) devuelve una lista ordenada de los valores de la secuencia

#https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch14s07.html


