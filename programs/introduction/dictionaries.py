#Creating a Dictionary:
students={
        'name':'Achu Jozef',
        'age':24,
        'place':'Kattakada',
        'course':'Software'
          }
#Accessing Values:
name=students['name']
age=students.get('age')

#Updating Values:
students['age']=99
students.update({'course':'Engineer','job':'Software'})

#Adding New Key-Value Pairs:
students['Height']=183
print(name,age,students['course'],students['job'])

#Removing Key-Value Pairs:
del students['age']
students.pop('course')

#Iterating Through Keys and Values:
for key in students:
    print(key,students[key])


for key , value in students.items():
    print(key,value)

print(students.items())


#Checking if a Key Exists:
x='nme'
if x in students:
    print("Yes")
else:
    print("No")

#Getting All Keys and Values:

keys=students.keys()
values=students.values()
print(keys,values)

#Copying Dictionaries:
student_copy = students.copy()  # Shallow copy

#Clearing a Dictionary:
student_copy.clear()
print(student_copy)

#Default Values with get():
a=students.get('nae','abcd')
print(a)

#Dictionary Comprehension:
numb=[1,2,3,4,5]
sqRt={num:num**2 for num in numb}
print(sqRt.items())

#Converting a List to a Dictionary:
fruits= ['apple','banana','pinaple']
dict_fruits={fruit:len(fruit) for fruit in fruits}
print(dict_fruits)

#Swapping Keys and Values:
original = {"a": 1, "b": 2, "c": 3}
swapped={value:key for key,value in students.items()}
print(swapped)

#Conditional Transformations:
trans={num:'even' if num%2==0 else 'odd' for num in numb}
print(trans)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}  # Using dictionary unpacking
print(merged_dict)