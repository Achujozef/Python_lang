# Converts to lowercase: "hello, world!"
text="       HELLO WORLD"
x=text.lower()
print(x)
# Converts to uppercase: "HELLO, WORLD!"
x=x.upper()
print(x)
x=x.strip()# Removes leading/trailing whitespace
print(x)
x=x.replace("HELLO", "Hi")  # Replaces "Hello" with "Hi": "Hi, World!"
print(x)
x=x.split(",")        # Splits into a list: ['Hello', ' World!']
print(x)

#String Formatting:

name='Achu'
place="KTDA"

out=f"my name is {name} and \ni'am from {place}"
print(out)
words="i am a disco dance \n ohoho"
print(words)
