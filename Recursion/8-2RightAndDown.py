"""
8.2
Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can
only move in two directions: right and down. How many possible paths are there for
the robot?
FOLLOW UP
Imagine certain squares are "off limits", such that the robot can not step on them.
Design an algorithm to get all possible paths for the robot.
"""

# Since it is N x N, there are N - 1 number of moves for each direction
# Therefore each path has (X - 1) + (Y - 1) steps


def calc(x,y,matrix):
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return 0 #out of border/range
    # elif matrix[x][y] == 1:
    #     return 0 # this cell has been already visited (only have to worry if we can go
    #     left,up,right,down)
    elif x == len(matrix) - 1 and y == len(matrix[0]) - 1:
        print 'end reached'
        return 1 # reached destination (last cell)
    else:
        matrix[x][y] = 1 # mark as visited
        # create copies of matrix for the recursion calls
        m1 = list(matrix)
        m2 = list(matrix)
        for i in matrix:
            string = ""
            for j in i:
                string += str(j)
            print string
        print '\n'
        return calc(x+1,y,m1) + calc(x,y+1,m2)

def move_robot(n):
    # an un-visited cell will be marked with "0"
    matrix = [[0]*n for x in xrange(n)]
    return calc(0, 0, matrix)

print move_robot(4)

