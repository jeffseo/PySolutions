"""
5.1
You are given two 32-bit numbers, N and M, and two bit positions, i and j. 
Write a method to set all bits between i and j in N equal to M 
(e.g., M becomes a substring of N located at i and starting at j).
EXAMPLE:
Input: N = 10000000000, M = 10101, i = 2, j = 6
Output: N = 10001010100
"""

def SetBinaryBetween(N,M,i,j):
    if i > j:
        return
    
    print bin(N)
    print bin(M)

    test = str(bin(N))
    n1 = []
    for itr, bit in enumerate(test):
        if itr >= i and itr <= j:
            if bit == '1':
                bit = '0'
        n1.append(bit)

    print test
    print n1

    print bin(N)

SetBinaryBetween(1024,21,2,6)