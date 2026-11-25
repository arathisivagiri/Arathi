# Print out all colors from color-list1 not contained in color-list2

list1 = ['red', 'blue', 'green', 'black']
list2 = ['red', 'black']
for color in list1:
    if color not in list2:
        print(color)
