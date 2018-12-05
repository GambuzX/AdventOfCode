file = open("input.txt")
polymer = file.read()
file.close()
poly_chars = []

for c in polymer:
    poly_chars.append(c)

del poly_chars[-1]

changed = True
while changed:
    changed = False
    index = 0
    iterations = len(poly_chars)-1
    skip_1 = False
    skip_2 = False
    for counter in range(iterations):
        if skip_1:
            skip_1 = False
        elif skip_2:
            skip_2 = False
        elif abs(ord(poly_chars[index]) - ord(poly_chars[index+1])) == 32:
            del poly_chars[index:index+2]
            skip_1 = True
            changed = True
            if index == 0:
                skip_2 = True
            else:
                index -= 1
        else:
            index += 1
print("Remained units {0}".format(len(poly_chars)))
