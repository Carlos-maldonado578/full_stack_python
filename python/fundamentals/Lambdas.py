def square(num):
    x = num ** 2
    return x

lambda num: num ** 2
lambda num1, num2 : num1 + num2

# create a new list, with a lambda as an element
my_list = ['test_string', 99, lambda x : x ** 2]
# access the value in the list
print(my_list[2]) # will print a lambda object stored in memory
# invoke the lambda function, passing in 5 as the argument
print(my_list[2](5))

print()

# define a function that takes one input that is a function
def invoker(callback):
    # invoke the input pass the argument 2
    print(callback(2))
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

add10 = lambda x: x + 10 # store lambda expression in a variable
print(add10(2))  # returns 12
print(add10(98)) # returns 108


def incrementor(num):
    start = num
    return lambda x: num + x

# create a list
my_arr = [1,2,3,4,5]
# define a function that squares values
def square(num):
    return num ** 2
# invoke map function
print(list(map(square, my_arr)))

my_arr = [1,2,3,4,5]
print(list(map(lambda x: x ** 2, my_arr))) # invoke map, pass in a lambda as the first argument




