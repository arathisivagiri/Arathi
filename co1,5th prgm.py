# Prompt the user for a list of integers. For all values greater than 100, store 'over' instead

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    x = int(input("Enter integer: "))
    if x > 100:
        lst.append("over")
    else:
        lst.append(x)
print("Result :", list)
