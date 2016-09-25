"""
Given an integer, print the next smallest and next largest number that have the same
number of 1 bits in their binary representation.
"""

INT_MAX = 0xFFFFFFFF
# Brute force
def brute_force(N):
    numOfOneBits = str(bin(N)[2:]).count('1')
    itr = N + 1
    smallest = 0
    largest = 0
    while itr <= INT_MAX:
        if numOfOneBits == str(bin(itr)[2:]).count('1'):
            smallest = itr
            break
        itr += 1

    print smallest

    itr = N + 1
    while itr <= INT_MAX:
        if numOfOneBits == str(bin(itr)[2:]).count('1'):
            largest = itr
        itr += 1

    print largest

# Pg 58 of CtCi has another solution (Non-brute force)

brute_force(6)