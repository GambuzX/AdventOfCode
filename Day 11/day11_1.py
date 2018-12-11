serial_number = 3214 # puzzle input

fuel_cells = []
for y in range(1, 301):
    for x in range(1, 301):
        rack_id = x + 10
        power_level = rack_id * y
        power_level += serial_number
        power_level *= rack_id
        if len(str(power_level)) < 3:
            power_level = 0
        else:
            power_level = int(str(power_level)[-3::])
        power_level -= 5
        fuel_cells.append(power_level)


max_power_found = 0
max_power_x = 0
max_power_y = 0
max_size = 0
for y in range (0, 298):
    for x in range(0, 298):
        
        total = 0
        total += fuel_cells[300 * y + x]
        total += fuel_cells[300 * y + x + 1]
        total += fuel_cells[300 * y + x + 2]
        total += fuel_cells[300 * (y + 1) + x]
        total += fuel_cells[300 * (y + 1) + x + 1]
        total += fuel_cells[300 * (y + 1) + x + 2]
        total += fuel_cells[300 * (y + 2) + x]
        total += fuel_cells[300 * (y + 2) + x + 1]
        total += fuel_cells[300 * (y + 2) + x + 2]
        if total > max_power_found:
            max_power_found = total
            max_power_x = x + 1
            max_power_y = y + 1

print("Max power found was {0} for x = {1}, y = {2}".format(max_power_found, max_power_x, max_power_y))