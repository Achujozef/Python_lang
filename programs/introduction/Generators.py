def Generators():
    yield 1
    yield 2
    yield 3

value=Generators()

print(value.__next__())
print(value.__next__())
print(value.__next__())


def prefSqrt():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

value = prefSqrt()

for i in value:
    print(i)
