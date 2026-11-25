#(a)Generate positive list of numbers from a given list of integer

numbers = [i for i in [1, -1, 2, -2, 3, -3] if i > 0]
print("(a) Positive numbers:", numbers)

#(b)Square of N numbers

square = [n * n for n in[1,2,3,4,5]]
print("(b) Square of numbers:", square)

#(c)Form a list of vowels selected from a given word
str=input("enter a word")
vowels=[i for i in str if i.lower()in "aeiou"or i.upper() in "AEIOU"]
print(vowels)

#(d)List ordinal value of each element of a word (using ord() to ger ordinal values)

str=input("enter a word:")
b=[ord(char)for char in str]
print("ordinary values",b)
