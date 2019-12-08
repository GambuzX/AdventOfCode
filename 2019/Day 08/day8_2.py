from PIL import Image, ImageDraw

color_map = {
	'0' : (0, 0, 0),
	'1' : (255, 255, 255)
}

width = 25
height = 6
layer_size = width * height

with open('input.txt', 'r') as handle:
	pixels = handle.read()

layers = [pixels[i:i+layer_size] for i in range(0, len(pixels), layer_size)]

decoded = [['?' for i in range(width)] for j in range(height)]
for row in range(height):
	for col in range(width):
		color_offset = row*width + col
		color = layers[0][color_offset]

		layer_i = 1
		while color == '2' and layer_i < len(layers):
			color = layers[layer_i][color_offset]
			layer_i += 1

		decoded[row][col] = color

		
img = Image.new('RGB', (width, height), "green")
pixels = img.load()


for row in range(height):
	for col in range(width):
		pixels[col, row] = color_map[decoded[row][col]]

img.show()
