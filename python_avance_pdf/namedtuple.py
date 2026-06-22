from collections import namedtuple 

"""@KevinManda"""

Point2D= namedtuple('Point2D', ['x', 'y'])

p=Point2D(3, 5)

print(p.x+p.y)

