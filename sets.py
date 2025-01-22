# Python Sets
# A collection which is unordered, unchangeable, and unindexed
# Sets do not allow duplicates
# Sets are written with curly brackets

fruits = {'apple', 'banana', 'cherry'}
tropical = {'mango', 'papaya'}

fruits.add('orange')
fruits.update(tropical) # the update method changes the original set



fruits.discard('pineapple')

print(fruits)
