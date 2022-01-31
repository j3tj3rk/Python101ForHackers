# This module will cover reading and writing files. Python has standard functions for creating reading and writing to files. For example if we had a file that contained the most common top 100
# passwords, we could use python to open that file and iterate over those passwords
f = open('top-100.txt')
print(f)

# We could again open the same file and specify the mode of read text(rt)
f = open('top-100.txt', 'rt')
print(f)

# We can also read the file with the below command. Running this will read the file out in the command line
print(f.read())

# If we want to write to a file we can use the following
f = open("test.txt", "w")
f.write("test line")
f.close()

# We can now run cat test.txt to confirm that the file was created and the test text was written to the file.
# If we want to add text to the line we would use the append mode

f = open("test.txt", "a")
f.write("test line number 2")
f.close()
# Now run the file again and cat it out. We should have test line and test line number 2 written to the file

# To specify the name of the file, whether the file has been closed or not and the mode of the file we can run
print(f.name)
print(f.closed)
print(f.mode)

# The file we have been working with only has 100 lines so using read mode hasnt been a problem. However for larger files we can use the file object as an iterator. 

with open('rockyou.txt', encoding='latin-1') as f:
	for line in f:
		pass
