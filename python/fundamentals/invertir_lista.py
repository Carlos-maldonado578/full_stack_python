lenguajes = ["Go", "Rust", "C", "JavaScript", "PHP", "Python"]
print("Original", lenguajes)

lenguajes.reverse()
print("Reverse: ", lenguajes)#['Python', 'PHP', 'JavaScript', 'C', 'Rust', 'Go']

print(lenguajes[2:])
print(lenguajes[:2])
print(lenguajes[:])
print(lenguajes[::])
print(lenguajes[-2])
print()

invertidos = lenguajes[::-1]
print("Invertidos: ",invertidos)
