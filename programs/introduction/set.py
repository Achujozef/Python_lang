my_set = {1, 2, 3}   
empty_set = set()                 # Creating an empty set

#Adding and Removing Elements:

my_set.add(4)
my_set.update([1,2,3,4,5,6,7,8,9])
my_set.remove(3)
my_set.discard(50)
my_set.pop() #from index 0
print(my_set)
my_set.clear()

#Set Operations:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union=set1 | set2
print(' Union of two sets',union)
intersection= set1 & set2
print('Intersection of two sets',intersection)
difference= set1 - set2
print(' Set difference',difference)
symetric= set1^set2
print(' Symmetric difference',symetric)

print(set1.issubset(set2)) #Returns True if the set is a subset of the other set.
print(set1.isdisjoint(set2)) #Returns True if the sets have no common elements.
print(set1.issuperset(set2)) # Returns True if the set is a superset of the other set.
