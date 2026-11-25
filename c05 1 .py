with open("vi.txt","r") as fo:
    lines=fo.readlines()
    
print("orginal lines:",lines)
stripped_lines=[line.strip() for line in lines]
print("stripped lines:",stripped_lines)