# From a list of integers, create a list removing all even numbers.

list = list(map(int, input("Enter integers: ").split()))
result = []
for x in list:
    if x % 2 != 0:
        result.append(x)
print("List after removing even numbers:", result)
