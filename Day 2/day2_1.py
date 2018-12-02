twice_total = 0
thrice_total = 0

f = open("input.txt")

for line in f:
    letters = {}
    counted_twice = False
    counted_thrice = False

    for char in line:
        if char not in letters.keys():
            letters[char] = 1
        else:
            letters[char] += 1

    for key in letters:
        if letters[key] == 2 and not counted_twice:
            twice_total += 1
            counted_twice = True
        elif letters[key] == 3 and not counted_thrice:
            thrice_total += 1
            counted_thrice = True

checksum = twice_total * thrice_total
print checksum
