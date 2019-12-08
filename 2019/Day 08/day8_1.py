width = 25
height = 6
layer_size = width * height

def count_occurences(layer):
	counter = {}
	for c in layer:
		if c in counter.keys():
			counter[c] += 1
		else:
			counter[c] = 1
	return counter

with open('input.txt', 'r') as handle:
	pixels = handle.read()

layers = [pixels[i:i+layer_size] for i in range(0, len(pixels), layer_size)]

best_counter = {'0': 99999}
for layer in layers:
	cnt = count_occurences(layer)
	if cnt['0'] < best_counter['0']:
		best_counter = cnt

print(best_counter['1'] * best_counter['2'])

