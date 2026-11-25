#Count the occurrences of each word in a given line of text

s = input("Enter a line: ")
words = s.split()
for word in set(words):
    print(word, ":", words.count(word))
 
