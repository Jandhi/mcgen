from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
import time

air_ids = [0, 17, 18, 37, 38, 39, 40, 83, 86, 106, 111, 162, 175]
water_ids = [8, 9, 79]

x_plus = 0
x_minus = 1
z_plus = 2
z_minus = 3

class Map:

	def __init__(self, box, level):
		print('GENERATING MAP')
		tic = time.time()
		self.size = (abs(box.maxx - box.minx), abs(box.maxy -box.miny), abs(box.maxz - box.minz))
		self.origin = (box.minx, box.miny, box.minz)

		self.height =[[0 for z in range(self.size[2])] for x in range(self.size[0])]
		self.water =[[False for z in range(self.size[2])] for x in range(self.size[0])]


		for x in range(self.size[0]):
			for z in range(self.size[2]):
				for y in reversed(range(self.size[1])):
					id = level.blockAt(x + self.origin[0], y + self.origin[1], z + self.origin[2])
					if id not in air_ids:
						self.height[x][z] = y
						if id in water_ids:
							self.water[x][z] = True
						break


		toc = time.time()
		print('GENERATING MAP TOOK %.2f SECONDS' %(toc - tic))


	def is_rough(point, dir):
		x, y, z = point
		if dir == x_plus:
			return x + 1 >= self.size[0] or abs(self.height[x][z] - self.height[x+1][z]) >= 2   
		elif dir == x_minus:
			return x - 1 < 0 or abs(self.height[x][z] - self.height[x-1][z]) >= 2
		elif dir == z_plus:
			return z + 1 >= self.size[2] or abs(self.height[x][z] - self.height[x][z+1]) >= 2
		elif dir == z_minus:
			return z - 1 < 0 or abs(self.height[x][z] - self.height[x][z-1]) >= 2









