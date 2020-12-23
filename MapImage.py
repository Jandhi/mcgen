import time
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from PIL import Image
from map import Map


inputs = (
)

def perform(level, box, options):
	start_time = time.time()

	print("----------------")
	print("BEGINNING FILTER")

	map = Map(box, level)

	show_height_map(map.height, 4)
	show_water_map(map.water, 4)

	print("\nDone (total time elapsed: %i s)." % (time.time() - start_time,))

def show_height_map(height_map, upscale_factor):
	print("Generating height map image")
	img = Image.new('RGB', (len(height_map) * upscale_factor, len(height_map[0]) * upscale_factor), "white")  # create a new white image
	pixels = img.load()  # create the pixel map

	min_value = height_map[0][0]
	max_value = height_map[0][0]
	for i in xrange(0, len(height_map) - 1):
		for j in xrange(0, len(height_map[0]) - 1):
			min_value = min(min_value, height_map[i][j])
			max_value = max(max_value, height_map[i][j])

	for i in range(img.size[0]):  # for every col:
		for j in range(img.size[1]):  # For every row
			value = height_map[i//upscale_factor][j//upscale_factor]
			value = ((value - min_value) * 236) / (max_value - min_value) + 20
			pixels[i, j] = (value, value, value)  # set the colour accordingly

	img.show()

def show_water_map(water_map, upscale_factor):
	print("Generating water map image")
	img = Image.new('RGB', (len(water_map) * upscale_factor, len(water_map[0]) * upscale_factor), "white")  # create a new white image
	pixels = img.load()  # create the pixel map

	for i in range(img.size[0]):  # for every col:
		for j in range(img.size[1]):  # For every row
			if water_map[i // upscale_factor][j // upscale_factor]:
				pixels[i, j] = (0, 0, 255)  # set the colour accordingly

	img.show()

def show_roughness_border_map(x_roughness_map, z_roughness_map, upscale_factor):
	print("Generating roughness border map image")
	img = Image.new('RGB', ((len(x_roughness_map) * 2 + 1) * upscale_factor, (len(z_roughness_map[0]) * 2 + 1) * upscale_factor),
					"white")  # create a new white image
	pixels = img.load()  # create the pixel map

	for i in range(img.size[0]):  # for every col:
		for j in range(img.size[1]):  # For every row
			x = (i // upscale_factor) // 2
			z = (j // upscale_factor) // 2
			if (i // upscale_factor) % 2 == 1:
				if x_roughness_map[x][z]:
					pixels[i, j] = (0, 0, 0)
			if (j // upscale_factor) % 2 == 1:
				if z_roughness_map[x][z]:
					pixels[i, j] = (0, 0, 0)

	img.show()

roughness_colour = {
	0 : (255, 255, 255),
	1 : (255, 255, 77),
	2 : (255, 204, 0),
	3 : (255, 153, 51),
	4: (255, 51, 0)
}

def show_roughness_map(roughness_map, upscale_factor):
	print("Generating roughness map image")
	img = Image.new('RGB', (len(roughness_map) * upscale_factor, len(roughness_map[0]) * upscale_factor),
					"white")  # create a new white image
	pixels = img.load()  # create the pixel map

	for i in range(img.size[0]):  # for every col:
		for j in range(img.size[1]):  # For every row
			roughness = roughness_map[i // upscale_factor][j // upscale_factor]
			pixels[i, j] = roughness_colour[roughness]  # set the colour accordingly

	img.show()