#This is a comment
print("Hello World")

# VARIABLES
# Variables are containers for storing data values
x = 5
y = 10

# Variable Casting
z = str('Hello')
i = int(10)
j = float(3)
print(x)
print(y)

print(type(z))
print(type(i))
print(type(j))

a = "Python"
b = "is"
c = "awesome!"

print(a, b, c)
print("Hello","World")

n = "Awesome"

def myFunc():
    global n
    n = "Fantastic"
    print("Python is " + n)


myFunc()

print(n)