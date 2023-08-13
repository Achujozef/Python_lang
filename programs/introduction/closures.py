def outer(x):
    def inner(y):
        return x+y
    return inner

x=outer(5)
y=x(3)
print(y)