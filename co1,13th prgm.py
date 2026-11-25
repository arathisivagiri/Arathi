#Create a list of colors from comma-separated color names entered by the user. Display the first and last colors.

s = input("Enter colors separated by comma: ")
a = s.split(',')
print("First:", a[0].strip())
print("Last:", a[-1].strip())
