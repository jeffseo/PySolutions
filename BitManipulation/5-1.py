import sys
"""
5.1
You are given two 32-bit numbers, N and M, and two bit positions, i and j. 
Write a method to set all bits between i and j in N equal to M 
(e.g., M becomes a substring of N located at i and starting at j).
EXAMPLE:
Input: N = 10000000000, M = 10101, i = 2, j = 6
Output: N = 10001010100
"""
INT_MAX = 0xffffffff
def updateBits(n,m,i,j):
    print "\nAnswer from CtCi:"
    n1 = list(str(bin(INT_MAX)[2:]))
    mask_left = INT_MAX - ((1 << j) - 1)
    mask_right = (1 << i) - 1

    mask = mask_left | mask_right
    result = ((n & mask) | (m << i))
    print "N = " + str(bin(result)[2:])


def SetBinaryBetween(N,M,i,j):
    print "my method:"
    if i > j:
        return

    stringN = str(bin(N)[2:])
    stringM = str(bin(M)[2:])

    print "Before:"
    print "N = " + stringN
    print "M = " + stringM
    n1 = []

    # 0 out the values in N from i to j
    for itr, bit in enumerate(reversed(stringN)):
        if itr >= i and itr <= j:
            if bit == '1':
                bit = '0'
        n1.append(bit)

    itr = i
    for bit in reversed(stringM):
        n1[itr] = bit
        itr += 1

    n1.reverse()
    print "\nAfter:"
    print "N = " + "".join(n1)

SetBinaryBetween(1024,21,2,6)
updateBits(1024,21,2,6)
