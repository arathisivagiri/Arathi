#Accept a file name from the user and print the extension of that file.

s = input("Enter a file name: ")
print("Extension of the file:", s.split('.')[-1])
