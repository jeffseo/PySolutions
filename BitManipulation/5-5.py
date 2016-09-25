"""
Write a function to determine the number of bits required to convert integer A to
integer B.
Input: 31, 14
Output: 2
"""

def numOfBitSwapRequired(A,B):
    count = 0
    c = A ^ B
    while c != 0:
        count += c & 1
        c = c >> 1

    print count
numOfBitSwapRequired(5,0)