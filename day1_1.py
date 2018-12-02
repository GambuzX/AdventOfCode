total = 0

f = open("input.txt")

for line in f:
    if line[0] == '+':
        total += int(line[1::])
    else:
        total -= int(line[1::])

print total
