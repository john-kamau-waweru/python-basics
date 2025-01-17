# Python Strings
x = "Hello World"

print(len(x))

txt = "Python is awesome and easy to learn"
print("awesome" in txt)

# Slicing Strings
a = "Hello World"
print(a[2:5])

# Modify strings
simpleWord = " Simple Word "
print(simpleWord.upper())
print(simpleWord.lower())
print(simpleWord.strip())
print(simpleWord.replace("Word", "World"))
print(simpleWord.strip().split(" "))

# String Concatenation
i = "Hello"
j = "Kenya"

k = i + " " + j
print(k)

age = 30
simpleText = f"My name is John and I am {age}"
print(simpleText)