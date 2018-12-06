import re

file = open("input.txt")
coords = []
for line in file:
    coords.append(line[:-1:])
file.close()


def x(coord):
    return int(re.search("([0-9]*)(,)", coord).group(1))


def y(coord):
    return int(re.search("(,\s)([0-9]*)", coord).group(2))


map_side = 400
map = [-1 for i in range(map_side**2)]

for index, point in enumerate(map):
    point_x = index % map_side
    point_y = int(index / map_side)

    total_dist = 0
    for letter_i, coord in enumerate(coords):
        dist = abs(x(coord) - point_x) + abs(y(coord) - point_y)
        total_dist += dist

    if total_dist < 10000:
        map[index] = '#'

region_size = 0
for point in map:
    if point == '#':
        region_size += 1

print(region_size)