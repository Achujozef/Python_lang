x=int("123")
x=x+50
print(x)


try:
    result=10/5
    print(result)
except ZeroDivisionError:
    print("Division Error")
else:
    print("ellam Nallathinu")
finally:
    print("kazhinju")