from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from utility import fill

def perform(level, box, options):
    point1 = (box.minx, box.miny, box.minz)
    point2 = (box.maxx, box.maxy, box.maxz)
    fill(point1, point2, level)