"""
9.3
Given a sorted array of n integers that has been rotated an unknown number of
times, give an O(log n) algorithm that finds an element in the array. You may assume
that the array was originally sorted in increasing order.
EXAMPLE:
Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
Output: 8 (the index of 5 in the array)
"""

def modifiedBinarySearch(array, value):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (right + left) / 2
        if array[middle] == value:
            return middle
        elif array[left] <= array[middle]:
            if value > array[middle]:
                left = middle + 1
            elif value >= array[left]:
                right = middle - 1
            else:
                left = middle + 1
        elif value < array[middle]:
            right = middle - 1
        elif value <= array[right]:
            left = middle + 1
        else:
            right = middle - 1

    return None

def findElement(array, value):
    return modifiedBinarySearch(array, value)    


t1 = [15,16,19,20,25,1,3,4,5,6,7,10,14]
print findElement(t1, 5)