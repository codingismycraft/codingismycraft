"""Solves the container with most water problem.

See also:
https://medium.com/@monisha.mary.mathew/container-with-most-water-477ee813a7f9
"""

import collections

Point = collections.namedtuple("Point", ['x', 'y'])

def get_max_area(points):
    i1 = 0
    i2 = len(points) - 1
    max_area = 0
    while points[i1].x < points[i2].x:
        height = min(points[i1].y, points[i2].y)
        width = points[i2].x - points[i1].x
        max_area = max(max_area, height * width)
        if points[i1].y > points[i2].y:
            i2 -= 1
        else:
            i1 += 1
    return max_area
