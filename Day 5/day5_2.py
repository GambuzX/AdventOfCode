file = open("input.txt")
polymer = file.read()
file.close()
poly_chars = []

for c in polymer:
    poly_chars.append(c)
del poly_chars[-1]

min_size = 999999
for c in range(ord('a'), ord('z')+1):
    poly_copy = poly_chars
    poly_copy = list(filter(lambda ch: ch != chr(c) and ch != chr(c-32), poly_copy))

    changed = True
    while changed:
        changed = False
        index = 0
        iterations = len(poly_copy) - 1
        skip_1 = False
        skip_2 = False
        for counter in range(iterations):
            if skip_1:
                skip_1 = False
            elif skip_2:
                skip_2 = False
            elif abs(ord(poly_copy[index]) - ord(poly_copy[index + 1])) == 32:
                del poly_copy[index:index + 2]
                skip_1 = True
                changed = True
                if index == 0:
                    skip_2 = True
                else:
                    index -= 1
            else:
                index += 1

    if len(poly_copy) < min_size:
        min_size = len(poly_copy)

print("Minimum size is {0}".format(min_size))
