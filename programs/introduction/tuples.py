my_tuple = (1, 2, 3)

subset_tuple = my_tuple[1:3]  # Creates a new tuple (2, 3)

new_tuple=my_tuple+(4,5)
print(new_tuple)

rep_tuple= new_tuple*2
print(rep_tuple)

x=rep_tuple.count(2)
print(x)

y=rep_tuple.index(5)
print(y)

a,b,c,d,e,f,g,h,i,j=rep_tuple