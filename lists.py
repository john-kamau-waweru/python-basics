# Python Lists
# Lists are used to stroe multiple items in a single variable
# Created using square brackets []

basicList = ["apple", "banana", "banana", "orange", "apple", "pineapple", "avocado"]

print(basicList)
print(len(basicList))
print(type(basicList))
print(basicList[2:5])

if "apple" in basicList:
    print("Yes, apple is in the fruits list")

# Lists are ordered(have indexes), changable and can have duplicates
basicList[1] = "kiwi"
print(basicList)

# Add list items
basicList.append("Watermelon") # add item at the end of a list
print(basicList)

basicList.insert(1, "berry")
print(basicList)

tropical = ["mango", "papaya"]
basicList.extend(tropical)
print(basicList)


# Remove list items
basicList.remove("papaya")
print(basicList)

basicList.pop(0)
print(basicList)

# Loop through a list

for x in basicList:
    print(x)

print("******************************************************")

print(range(len(basicList)))

print("******************************************************")

for i in range(len(basicList)):
    print(basicList[i])

print("******************************************************")

m = 0
while m < len(basicList):
    print(basicList[m])
    m = m + 1