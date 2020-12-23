from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from utility import fill
from material import WeightedMaterial

def perform(level, box, options):
    point1 = (box.minx, box.miny, box.minz)
    point2 = (box.maxx, box.maxy, box.maxz)

    material = WeightedMaterial( [((4, 0), 3) , ((48, 0), 1)] )

    fill(point1, point2, level, material)