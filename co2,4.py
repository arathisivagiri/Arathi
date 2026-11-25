# Generate a list of four-digit numbers in a given range with all their digits even and the number is a perfect square.

a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for n in range(a, b + 1):
    if 1000 <= n <= 9999 and int(n ** 0.5) ** 2 == n and all(int(d) % 2 == 0 for d in str(n)):
        print(n, end=", ")
print()
