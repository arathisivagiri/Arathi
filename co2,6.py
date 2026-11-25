# Count the number of characters (character frequency) in a string.
s = input("Enter a string: ")
for i in sorted(set(s)):
    print(f"{i} : {s.count(i)}")
OUTPUT 
