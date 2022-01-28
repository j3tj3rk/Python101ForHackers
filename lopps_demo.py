a = 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a) # This a loop but it is not an efficient way to write code. We can replace this terrible method with loops

a = 1
while a < 5:
	a += 1
	print(a)

# Another type of loop is a for loop

for i in [0, 1, 2, 3, 4, 5]:
	print(i+6)

print("--------------------------")

# We can also use range loops
for i in range(5):
	print(i+6)
