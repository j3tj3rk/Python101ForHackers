dict1 = {"a":1, "b":2, "c":3}
print(dict1)
print(type(dict1))
print(len(dict1))

print(dict1["a"])

# We can print all of the dictionary keys with 
print(dict1.keys())

# We can print out the values of this dictionary
print(dict1.values())

# We can also print out all of the items
print(dict1.items())

# Dictionaries do not allow duplicates but we can add new items
dict1["d"] = 4
print(dict1)

# We can also change the key:value pairs
dict1["a"] = 0 
print(dict1)

# We can also remove items
dict1.pop("d")
print(dict1)

del dict1['c']
print(dict1)


# W3 can create empty dictionaries for later use
dict2 = {}
print(dict2)

dict3 = dict()
print(dict3)
