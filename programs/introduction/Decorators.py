
def decorator(fun):

    def inner(a,b):
        a=a-1
        b=b-1
        return fun(a,b)
    return inner
@decorator
def multi(a,b):
    return a*b


x=multi(10,20)
print(x)


def deco(fun):
    def inner(word):
        x=word.upper()
        return fun(x)
    return inner

@deco 
def upr(word):
    print (word)
 
upr('achu')