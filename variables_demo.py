# This module covers variables and data types. Variables are ways to store data in named locations. When you create a variable you are allocating space
# for that variables data to be stored depending on the data type. When creating a variable we use the = sign to assign a value. If we want to create a 
# variable called name and assign it the value of neut it would look like this:
name = "neut"
#Then we can print the variable with the python built in print function. 
print(name)

# We dont always have to define variables as strings. For example if we wanted to define the variable of name_length to represent the lenght of the name string.
# We wouldn't want that variable to be a string, we want it to be an integer. To define an integer we type the number in directly. It will look like this:

name_length = 4
print(name_length)

# Python also supports multiple assignment. Name and name_length can be defind in one line using  a comma in the syntax
# name, name_length = "neut", 4 (the example to the left has been commented out but will do the same thing as lines 5,6,11 and 12)

# We can also identify the specific types that have been assigned to the variables using the built in print function.
print(type(name))
print(type(name_length))

# Python also supports casting. If you want to explicitaly cast the type of data that you intended to enter, python supports that too. We can redefing
# name_length to be a string. By putting the 4 in brackets python is now interpreting the data as the string containing the value 4
name_length = "4"
print(type(name_length))

# We can explicity type this data by using int in brackets and pythong will now interpret this data as an integer
name_length = int("4")
print(type(name_length))

# When we are casting data we need to make sure that the cast makes sense. So name = int("neut") wouldnt make sense because neut isnt an integer. It is a 
# string.
# variables are case sensitive 
name_length = 4 # and
Name_length = 5 # are both different variables. 

# So far we have only played around with strings and integers. Python supports other data types such as list, tuples, dictionaries, booleans, ranges and
# bytes. Lets declare each of these so we know what they look like. 
# Let's start with list. We declare lists by using brackets[]
name_list = ["neut", "BLSCTF", "kerryisawesome"] # we can then verify the type of this data
print(type(name_list)) #this list has only three items but we can add more itesm by appending more commas and more values. 

# we can unpack the list above with the following
name1, name2, name3 = name_list
print(name1)
print(name2)
print(name3)

# We can also create a variable which is of type tuple. 
name_tuple = ("neut2", "BLSCTF2", "kerryisawesome2")
print(type(name_tuple)) # Note the type of the tuple will only print if you run this code. You will need to tell python to print the tuple with
# print(name_tuple) to get the tuple to print

# We can also create a dictionary
name_dictionary = {"neut": 4, "BLSCTF3": 7}
print(type(name_dictionary))

# We can also create a boolean and print out the type
name_boolean = False
print(type(name_boolean)) # The boolean can only have two types of values, true or false

# We can also create a range variable and print the type
name_range = range(6)
print(type(name_range))

# We can also assign a variable of type bytes and print the type
name_bytes = b"neut2"
print(type(name_bytes))

# Now that we have seen each of these class types we can also just print out the variables to see what the different data types look like when we print
# them out. Lets print these out with 
print(name_tuple)
print(name_list)
print(name_dictionary)
print(name_boolean)
print(name_range)
print(name_bytes)
