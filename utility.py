from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *

def fill(point1, point2, level):
    for x in range( abs(point1[0] - point2[0]) ):
        px = min(point1[0], point2[0]) + x

        for y in range( abs(point1[1] - point2[1]) ):
            py = min(point1[1], point2[0]) + y

            for z in range( abs(point1[2] - point2[2]) ):
                pz = min(point1[2], point2[2]) + z

                stone = 1
                level.setBlockAt(px, py, pz, stone)