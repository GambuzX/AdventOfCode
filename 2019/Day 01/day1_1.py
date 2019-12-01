with open("input.txt", 'r') as handle:
    vals = handle.read().split('\n')

print(sum([int(int(val)/3)-2 for val in vals]))
