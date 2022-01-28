# This module will cover numbers in python
t1_int = 1
t1_float = 1.0

print(t1_int)
print(t1_float)

# We can very these types by printing the type
print(type(t1_int))
print(type(t1_float))

# Floats are useful when we want to store floating point numbers. Which are values that may contain decimal places. 
# Integers are used when we only want to store integral whole numbers. 
# Be aware of this assignment when we are doing different things with the variables that we are using. For example if we want to print the numbers out or add them together as part of our script. 

# Python also supports complex numbers
t1_complex = 3.14j
print(t1_complex)
print(type(t1_complex))

# With numbers we are used to counting in base10. Python doesnt care what number system we use as long as we are consistent. 
# We can print in hex representation
t1_hex = 0xa
print(t1_hex)
print(type(t1_hex))

# We can also use an octal representation
ti_octal = 0o10
print(ti_octal)
print(type(ti_octal))

# We can add an integer to a hex number and an octal number
print(1 + 0x1 + 0o1)

# We can print in absolute value. Which will print the distance between the number and 0. 
print(abs(4))
print(abs(-4))

# Python also has a built in function to round a number so if we are working with a float and want to round that number to an integer we can use the round function
print(round(8.4))
print(round(8.5))
print(round(8.6))

# We can also use bin to print out the binary value of a number
print(bin(8))

# Or the hexadecimal representation of the number
print(hex(8))
