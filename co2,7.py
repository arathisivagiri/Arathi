# Add 'ing' at the end of a given string. If it already ends with 'ing', then add 'ly'.
s = input("Enter a string: ")
if len(s) < 3:
    print(s)
elif s.endswith("ing"):
    print(s + "ly")
else:
    print(s + "ing")
