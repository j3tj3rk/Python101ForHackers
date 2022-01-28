# Tuples can store multiple items in a single variable. Like strings, tuples are immutable and can not be changed. Tuples are a good data type to use when you know the data is fixed and won't change

tuple_items = ("item1", "item2", "item3")
print(tuple_items)
print(type(tuple_items))

# Tuples dont have to be strings. 
tuple_number =  (1, 2, 3)
print(tuple_number)
print(type(tuple_number))

# We can create a tuple with a number of items by using the overloaded * operator
tuple_repeat = ('Combine!', ) * 4
print(tuple_repeat)
print(type(tuple_repeat))

# We can create mixed tuples as well
mixed_tuple = ("A", 1, ("A", 1))
print(mixed_tuple)
print(type(mixed_tuple))

# Because tuples are immutable they can be combined but they can not be changed
# We can combine tuples
tuple_combined = tuple_items + tuple_number
print(tuple_combined)
print(type(tuple_combined))

# When working with tuples it can be useful to unpack them all in one line. For instance if we wanted to assign item1, item2 and item3 from the tuple_item

item1, item2, item3 = tuple_items
print(item1)
print(item2)
print(item3)

# When working with tuples it can be useful to know if items exist in the tuple or not. We can check if item2 is in the tuple_items tuple
print("item2" in tuple_items)
print("item4" in tuple_items)

# We can also find out the index of the match
print(tuple_items.index("item2"))
# We can reference these items based on their index
print(tuple_items[0])
print(tuple_items[1])
print(tuple_items[2])

# We can also print the length of a tuple
print(len(tuple_items))

# If we wanted to print out the last item in the tuple
print(tuple_items[-1])

# When working with indexes python also lets us make slices
print(tuple_items[0:2])
