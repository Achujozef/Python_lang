
from functools import reduce
x = 10

def modify_global():

    global x
    x += 5

modify_global()
print(x) 


# Arbitrary Number of Arguments:

# You can define functions that accept a variable number of arguments using *args (for non-keyword arguments) and **kwargs (for keyword arguments).

def print_arg(*args, **kwargs):
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key, value)

print_arg(1,2,3,4,5,a=9,b=8,c=7,d=6)

list1=[1,2,3,4,5,6,7,8,9]

x= set([i for i in list1 if i%2==0])
print(x)

evens=set(filter(lambda n: n%2==0,list1))
print(evens) 

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, numbers)
squares=set(squares)
print('squares',squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=filter(lambda x: x%2==0, numbers)
print(list(even))


def outer():
    def inner():
        pass

