# We can define a string variable using double quotes
string1 = "I am a string"
# We can also define strings using single quotes
string2 = 'I am a string too!'
# We can print our each of these strings and see that Python uses the double and single quotes the same
print(string1)
print(string2)

# We can also define multi line strings with three double quotes
string3 = """I am a long
long
string!"""

print(string3)

# If we want to print a string with a quote we need to escape the quote by using a back slash
string4 = "I\"m a string"
print(string4)

# Using single quotes we can also escape the quotes with a backslash
string5 = 'I\'m a string'
print(string5)

# Quotes are not the only thing we need to escape in Python when working with strings. We can escape a new line character with \n
string6 = "I\"m a string\nI\"m on a newline!"
# If we want to print a backslash we want to escape that as well. 
string6 = "\\ \x41\x42\x43"
print(string6)

# If we wanted to assign a variable with 10 a's we can print it this way or
string7 = "aaaaaaaaaa"
print(string7)

# We can also print it out this way
string7 = "a" * 10
print(string7)

print(len(string7))

print("string" in string4)
print(string4.startswith("I"))
print(string4.startswith("n"))

print(string4.index("string"))

# We can print the string in all uppercase or all lowercase
print(string4.upper())
print(string4.lower())

# When taking data from files the data may be messy. We can clean it up with the strip function
messy_string = "      Messy string!      "
print(messy_string)
print(messy_string.strip())

# We can also use the replace function to replace data in the strings
print(messy_string.replace("!","?").strip())
print(messy_string.replace("string", "example"))

# We can also split to split the variable based on characters
print(messy_string.split(","))
print(messy_string.split())

# We can redefing string4 and print it with encoding. All string in python are in unicode. To print strings in different code use the below function
string4 = "I am a string!"
print(string4)
print(string4.encode())
print(string4.encode("utf-8"))

# rjust and ljust are other useful functions. To print out string4 with right justified with 25 spaces use the below
print(string4.rjust(25))
# We can also use X to cover the spaces to make it easier to read the amount of right justified characters
print(string4.rjust(25,"X"))

print(string4.ljust(25))
print(string4.ljust(25,"X"))

# Python strings are immutable. To change strings after they have been defined we need to create new strings when changing or trying to change an existing string
print("I am " + "a string")
print("String 4 is " + str(len(string4)) + " characters long")

# The + symbol is whats known as an overloaded operator. It will join strings together as well as do the maths if we ask it to
print(1 + 1)
print("1" + "1")
print(type("1" + "1"))

# Python will also format for us and insert the string inside the placeholder. {} are used for placeholders
print("string4 is {} characters long!".format(len(string4)))

print("{} {} {}".format(len(string4), 5.0, 0x12))
# The format method also allows us to specify the order that we want to the data to be printed
print("{0} {2} {1}".format(len(string4), 5.0, 0x12))
print("{length}".format(length=len(string4)))

# We can als work with defined formatted string literals by prepending an f to the print statement. A formatted string is just an expression that gets evaluated during execution.
# For example we can define the length variable and define it to be the length of string4. 
length = len(string4)
print(f"string4 is {length} characters long")

# We can specify it as a float. The 2 represents two decimal places. We can define the number of decimal places by changing the 2 to a 3 or 9 or whichever number we choose.
print("string4 is {length:.2f} characters long".format(length=len(string4)))
print("string4 is {length:.3f} characters long".format(length=len(string4)))
print("string4 is {length:.9f} characters long".format(length=len(string4)))


print("string4 is {length:x} characters long".format(length=len(string4)))
print("string4 is {length:b} characters long".format(length=len(string4)))
print("string4 is {length:o} characters long".format(length=len(string4)))

print("string4 is %d characters long!" % len(string4))
print("string4 is %f characters long!" % len(string4))
print("string4 is %x characters long!" % len(string4))
