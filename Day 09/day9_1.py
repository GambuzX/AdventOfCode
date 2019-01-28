import re

file = open("input.txt")
input_line = file.read()
file.close()

players_n = int(re.search("([0-9]*)(\splayers)", input_line).group(1))
last_marble = int(re.search("([0-9]*)(\spoints)", input_line).group(1))

players = {}
for i in range(players_n):
	players[i] = 0

def next_current_marble(curr_index, list_length, shift_amount):
	step = 1
	if shift_amount < 0:
		step = -1
	for i in range(abs(shift_amount)):
		curr_index += step
		if curr_index == list_length:
			curr_index = 0
		elif curr_index == -1:
			curr_index = list_length-1
	return curr_index


current_player = 0
marbles = []
current_marble_index = 0
for marble in range(last_marble):
	if len(marbles) == 0:
		marbles.append(marble)
		current_marble_index = 0
	elif marble % 23 == 0:
		players[current_player] += marble
		current_marble_index = next_current_marble(current_marble_index, len(marbles), -7)
		players[current_player] += marbles[current_marble_index]
		del marbles[current_marble_index]
		if current_marble_index == len(marbles)-1:
			current_marble_index = 0
	else:
		current_marble_index = next_current_marble(current_marble_index, len(marbles), 2)
		marbles.insert(current_marble_index, marble)

	current_player += 1
	if current_player == len(players):
		current_player = 0


max_score = 0
for elf in players:
	if players[elf] > max_score:
		max_score = players[elf]

print(max_score)