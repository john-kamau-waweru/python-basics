# String Data Type
first_name = "John"
last_name = "Doe"

print(type(first_name))
print(isinstance(first_name, str))
print("^^^^^^^^^^^^^^^^^^^")

# Constructor function
pizza = str("Peperoni")
print(type(pizza))
print(isinstance(pizza, str))

# Concatenation
fullname = first_name + " " + last_name
print(fullname)

# Casting
tea_cups = str(200)
print(type(tea_cups))
print(tea_cups)
print("****************************")
# String Methods
print(first_name.upper())
print(last_name.lower())
