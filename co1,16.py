# Create a single string separated with space from two strings by swapping the character at position 1.
a = input("Enter first string: ")
b = input("Enter second string: ")
x = a[1]
y = b[1]
a_new = a[0] + y + a[2:]
b_new = b[0] + x + b[2:]
print(a_new + " " + b_new)
