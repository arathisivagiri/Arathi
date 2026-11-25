# Find the biggest of 3 numbers entered by the user

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("biggest=", a)
elif  b >c:
    print("biggest=", b)
else:
    print("biggest=", c)
