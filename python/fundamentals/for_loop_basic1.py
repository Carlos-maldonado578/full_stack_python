# salida de numeros 1 al 150.
count = 0
while count <= 150:
    print(count)
    count += 1

#Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
multi = 5
while multi <= 1000:
    print(multi)
    multi += 5

#Contar, Dojo Way -
# imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar.
# Si es divisible por 10, imprima "Coding Dojo".

contar = 1
while contar <= 100:
    contar += 1
    if contar % 5 ==0:
        print("Coding")
        if contar % 10 == 0:
            print("Coding Dojo")
            continue
    else:
        print(contar)

#¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
big = 0
for x in range(0, 500000):
    if x % 2 != 0:
        print(x)
        big += x
print(big)

#Cuenta regresiva por cuatro : imprime números positivos a partir de 2018, cuenta atrás por cuatro.

for x in range(2018, 0, -4):
    print(x)
#Contador flexible : establece tres variables: lowNum, highNum, mult.
# Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult.
# Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)

lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)
