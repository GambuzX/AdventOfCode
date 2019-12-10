import math

def visible_asteroids(map, a_row, a_col):
    found = {}
    count = 0
    for row in range(len(map)):
        for col in range(len(map[0])):

            if row == a_row and col == a_col:
                continue

            if map[row][col] == '.':
                continue
            
            vec = [row - a_row, col - a_col]
            norm = math.sqrt(math.pow(vec[0], 2) + math.pow(vec[1], 2))
            normalized = [vec[0]/norm, vec[1]/norm]
            angle = math.acos(-normalized[0]) # up_vector = [-1, 0], row, column

            if normalized[1] < 0:
                angle = 2*math.pi-angle

            angle = round(angle, 4)

            if angle not in found.keys():
                count += 1
                found[angle] = []

            found[angle].append([row,col])
    
    return found

def distance_to(pos1, pos2):
    return math.sqrt(math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))


def find_200th_asteroid(map, pos):
    angles = list(map.keys())
    angles.sort()

    destroyed = 0
    curr_i = 0
    last_destroyed = [0,0]
    while destroyed < 200:
        curr_angle = angles[curr_i]
        curr_i = (curr_i + 1) % len(angles)

        # no more positions here
        if len(map[curr_angle]) == 0:
            continue
            
        destroyed += 1
        last_destroyed = map[curr_angle][0]
        del map[curr_angle][0]

    return last_destroyed


with open("input.txt", 'r') as handle:
    file_lines = handle.read().split("\n")

map = []
for line in file_lines:
    map.append(list(line))


best_map = {}
best_pos = [0,0]
for row in range(len(map)):
    for col in range(len(map[0])):
        if map[row][col] == '.':
            continue
        found_map = visible_asteroids(map, row, col)
        if len(found_map.keys()) > len(best_map.keys()):
            best_map = found_map
            best_pos = [row, col]

# sort by distance to center
for key in best_map:
    best_map[key].sort(key = lambda pos : distance_to(pos, best_pos))

last_pos = find_200th_asteroid(best_map, best_pos)
print(last_pos[0] + last_pos[1]*100)