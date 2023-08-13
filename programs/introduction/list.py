numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14]

#Accessing Elements:
print('numbers[0]',numbers[0])
print('mixed[-1]',mixed[-1]) # Access the last element using negative index

#Slicing Lists:
print(numbers[1:3]) # Slice elements from index 1 to 3 (not inclusive)
print(numbers[::-1])#reverce
print(numbers[2:])# Slice elements starting from index 2

#Appending and Extending Lists:
fruits.append("Orange")
fruits.extend(["grape","kiwi"])
print(fruits)

#Inserting Elements:
numbers.insert(2,99)
print(numbers)

#Removing Elements:
fruits.remove("grape")# Remove specific element
poped=fruits.pop()# Remove and return the last element
print(fruits)
print(poped)

#Finding Index of an Element:
index=fruits.index("cherry")
print(index)

#Checking Membership:
print("apple" in fruits)

#Counting Elements:
count=fruits.count('apple')
print(count)

#Sorting Lists:
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#Reversing a List:
numbers.reverse()
print(numbers)

#Copying Lists:
new_fruuits= fruits.copy()
print(new_fruuits)

#List Comprehensions:
#new_list = [expression&out for item in iterable if condition]

print([x**2 for x in range(1,20) if x%2==0])

words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]

numbers = [1, 2, 3]
tuples = [(x, x**2) for x in numbers]

#List Concatenation:
combined_list = numbers + fruits   # Concatenate two lists