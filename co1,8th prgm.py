#Get a string from an input string where all occurrences of the first character are replaced with '$', except the first character itself.

s= input("Enter a string: ")
result = s[0] + s[1:].replace(s[0], '$')
print("Result:", result)
