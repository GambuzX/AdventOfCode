with open('input.txt') as handle:
	wires = handle.read().split('\n')

wire1 = wires[0].split(',')
wire2 = wires[1].split(',')

# x, y, steps_so_far
wire1_pos = [[0,0,0]]
wire2_pos = [[0,0,0]]

def find_positions(wire, out):
	pos = [0,0,0]
	steps = 0
	for ele in wire:
		dir = ele[0]
		move = int(ele[1:])

		if dir == 'R':
			pos[0] += move
		elif dir == 'L':
			pos[0] -= move
		elif dir == 'D':
			pos[1] -= move
		elif dir == 'U':
			pos[1] += move

		pos[2] += move

		out.append(pos.copy())	

def distance(p1, p2):
	return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def crosses(p1, p2, wire_list):
	for i in range(len(wire_list)-1):
		pos1 = wire_list[i]
		pos2 = wire_list[i+1]

		min_x = min(pos1[0], pos2[0])
		max_x = max(pos1[0], pos2[0])
		min_y = min(pos1[1], pos2[1])
		max_y = max(pos1[1], pos2[1])

		# vertical wire
		if pos1[0] == pos2[0]:

			# horizontal wire
			if p1[1] == p2[1] and p1[1] >= min_y and p1[1] <= max_y and pos1[0] >= min(p1[0], p2[0]) and pos1[0] <= max(p1[0], p2[0]):
				wire1_steps = pos1[2] + abs(p1[1] - pos1[1])
				wire2_steps = p1[2] + abs(pos1[0] - p1[0])
				return [pos1[0], p1[1], wire1_steps + wire2_steps]

		# horizontal wire
		elif pos1[1] == pos2[1]:

			# vertical wire
			if p1[0] == p2[0] and p1[0] >= min_x and p1[0] <= max_x and pos1[1] >= min(p1[1], p2[1]) and pos1[1] <= max(p1[1], p2[1]):
				wire1_steps = pos1[2] + abs(p1[0] - pos1[0])
				wire2_steps = p1[2] + abs(pos1[1] - p1[1])
				return [p1[0], pos1[1], wire1_steps + wire2_steps]

	return False



find_positions(wire1, wire1_pos)
find_positions(wire2, wire2_pos)


min_found = 999999
steps = 0
for i in range(len(wire2_pos)-1):
	p1 = wire2_pos[i]
	p2 = wire2_pos[i+1]

	intersection = crosses(p1, p2, wire1_pos)
	if intersection != False:
		min_found = min([min_found, intersection[2]])

print(min_found)