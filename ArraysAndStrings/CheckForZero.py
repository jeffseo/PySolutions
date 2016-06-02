"""
1.7
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column is set to 0.

Note: if we simply iterate through the matrix and every time we
see a 0, set that row and column to 0, later on it will detect those 0s in the iterations
to follow and set their row/column to 0. The entire matrix would become 0s.

To work around this, maintain a list of rows/columns which had 0s in the matrix. Then make a 
second pass of the matrix and set cell values to zero if its row or column is within the list
"""

import random

def check_for_zero(array_2d):
    columns = len(matrix[0])
    rows = len(matrix)
    row_tracker = []
    column_tracker = []
    for x in range(columns):
        for y in range(rows):
            if array_2d[x][y] == 0:
                row_tracker.append(y)
                column_tracker.append(x)

    for x in range(columns):
        for y in range(rows):
            if x in column_tracker or y in row_tracker:
                array_2d[x][y] = 0

    return array_2d

if __name__ == '__main__':
    m = 5
    n = 5
    matrix = [[random.randrange(0,9) for x in range(m)] for y in range(n)]
    print matrix

    print check_for_zero(matrix)