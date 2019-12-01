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

    min_dist = 9999
    number = -1
    repeated = False

    for letter_i, coord in enumerate(coords):
        dist = abs(x(coord) - point_x) + abs(y(coord) - point_y)
        if dist == min_dist:
            repeated = True
        elif dist < min_dist:
            min_dist = dist
            number = letter_i
            repeated = False

    if not repeated:
        map[index] = number

border_symbols = []
for i in range(map_side):
    if map[i] not in border_symbols:
        border_symbols.append(map[i])
    if map[-i] not in border_symbols:
        border_symbols.append(map[-i])
    if map[map_side*i] not in border_symbols:
        border_symbols.append(map[map_side*i])
    if map[map_side - 1 + map_side*i] not in border_symbols:
        border_symbols.append(map[map_side - 1 + map_side*i])

points_map = {}
for point in map:
    if point not in border_symbols and point != -1:
        if point not in points_map:
            points_map[point] = 1
        else:
            points_map[point] += 1

maximum = 0
for point in points_map:
    if points_map[point] > maximum:
        maximum = points_map[point]

print(maximum)
