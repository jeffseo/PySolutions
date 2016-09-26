"""
8.6
Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a 2-dimensional array of Colors), a
point, and a new color, fill in the surrounding area until you hit a border of that color.
"""

# TODO
class colors:
    BLACK, WHITE, RED, YELLOW, GREEN = range(5)

def create2DArray(N):
    array = [[0] * N for i in xrange(N)]
    return array

print create2DArray(3)