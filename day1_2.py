total = 0

found_freqs = []

while True:
    f = open("input.txt")
    found = False

    for line in f:
        if total in found_freqs:
            found = True
            break

        found_freqs.append(total)

        if line[0] == '+':
            total += int(line[1::])
        else:
            total -= int(line[1::])
    if found:
        print (total)
        break

    print total

    f.close()


