with open("input.txt", 'r') as handle:
    vals = handle.read().split('\n')


def calculate_fuel(value):
    ret_val = int(value/3)-2
    return max(ret_val, 0)


total = 0
for val in vals:
    mass = int(val)
    while mass > 0:
        fuel = calculate_fuel(mass)
        mass = fuel
        total += fuel
print(total)

