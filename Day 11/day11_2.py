serial_number = 3214  # puzzle input

p_fuel_sums = [[0 for i in range(301)] for i in range(301)]
for y in range(1, 301):
    for x in range(1, 301):
        rack_id = x + 10
        power_level = rack_id * y + serial_number
        power_level *= rack_id
        if len(str(power_level)) < 3:
            power_level = 0
        else:
            power_level = int(str(power_level)[-3])
        power_level -= 5
        p_fuel_sums[y][x] = power_level + p_fuel_sums[y-1][x] + p_fuel_sums[y][x-1] - p_fuel_sums[y-1][x-1]

max_power_found = 0
max_power_x = 0
max_power_y = 0
max_side = 0
for side in range(1, 301):
    for y in range(side, 301):
        for x in range(side, 301):
            total = p_fuel_sums[y][x] - p_fuel_sums[y-side][x] - p_fuel_sums[y][x-side] + p_fuel_sums[y-side][x-side]
            if total > max_power_found:
                max_power_found = total
                max_power_x = x
                max_power_y = y
                max_side = side

print("Max power found was {0} for x = {1}, y = {2} and size {3}".format(max_power_found, max_power_x - max_side + 1, max_power_y - max_side + 1, max_side))