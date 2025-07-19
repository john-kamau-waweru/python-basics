import math

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
print("")
# String Methods
print(first_name.upper())
print(last_name.lower())

print("")

title = "menu"
print(title.center(20, "*"))
print("Coffee".ljust(16, "_") + "+1".rjust(5))
print("Muffin".ljust(16, "_") + "+4".rjust(5))
print("Cake".ljust(16, "_") + "+6".rjust(5))
print("")

# Numeric Data Types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))


print(math.pi)