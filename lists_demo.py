# Lists are another kind of sequence in python. With lists we can change the data once they are defined
list1 = ["A", "B", "C", "D", "E", "F"]
print(list1)

# Lists can be all of the data types
list2 = ["A", 1, 2.0, ["A"], [], list(), ("A")]
print(list2)

# Lists can be indexed just like tuples

print(list1[0])
print(list1[-1])
print(list2[3][0])
print(list2[3][-1])

# Lists can be changed
list1[0] = "X"
print(list1)

# We can also delete from the list
del list1[0]
print(list1)

# We can reinsert the list
list1.insert(0, "A")
print(list1)

# If we dont care about adding to the list based on index we can use append
list1.append("G")
print(list1)

# There are bultin functions we can use on list. For example we may want to know the max value of list1 and the min value of list1
print(max(list1))
print(min(list1))

# We may also want to find the index of different items in the list. 
print(list1.index("C"))

# We can also print lists in reverse
list1.reverse()
print(list1)

# We can also count inside lists
print(list1.count("A")) #This will count the A's in the list
list1.append("A")
print(list1)
print(list1.count("A"))

# Unlike tuples we can use the pop function to remove and return the last thing added to the list
list1.pop()
print(list1)

# We can also clear the list removing all values from the list
list1.clear()
print(list1)

# We can also sort lists
list4 = [8, 12, 33, 4, 6, 2, 18, 94]
print(list4)

list4.sort()
print(list4)

# We can also sort in reverse
list4.sort(reverse=True)
print(list4)

# Any changes made in a list1 will be made in list2 because they are referencing the same underlying data
list5 = list4
print(list4)
print(list5)

# If we decide in list5 we want to change one of the values
list5[2] = "X"
print(list5)

# If we print list4 it should be the same
print(list4)

# List4 also changes because these variables are referencing the same data. If we want to work on the same data but do different things to that data we need to make a copy of that data
list6 = list4.copy()
print(list4)
print(list6)

# Now in list6 lets change the data at the second index
list6[2] = "A"
print(list6)
print(list4)
# Now the data is only changed in list6 since we made a copy. In python if you want to work on the same data but perform different actions on that data you need to make sure to create a copy. 

# The map function is used to apply some function to all items in the list. 

list7 = ["1", "2", "3"]
print(list7)

list8 = list(map(float, list7))
print(list8)
# Here we took the data in list7 and applied the float function to create list8
