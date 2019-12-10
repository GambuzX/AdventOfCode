import math

def visible_asteroids(map, a_row, a_col):
    found = set()
    count = 0
    for row in range(len(map)):
        for col in range(len(map[0])):

            if row == a_row and col == a_col:
                continue

            if map[row][col] == '.':
                continue
            
            vec = [row - a_row, col - a_col]
            norm = math.sqrt(math.pow(vec[0], 2) + math.pow(vec[1], 2))
            normalized = [vec[0]/norm, vec[1]/norm] # x does not matter
            angle = math.acos(normalized[1]) # up_vector = [0, 1]
            angle = round(angle, 4)

            if normalized[0] < 0:
                angle = 2*math.pi-angle

            if angle in found:
                continue

            count += 1
            found.add(angle)
    
    return count


with open("input.txt", 'r') as handle:
    file_lines = handle.read().split("\n")

map = []
for line in file_lines:
    map.append(list(line))


max_found = 0
for row in range(len(map)):
    for col in range(len(map[0])):
        if map[row][col] == '.':
            continue
        max_found = max(max_found, visible_asteroids(map, row, col))

print(max_found)