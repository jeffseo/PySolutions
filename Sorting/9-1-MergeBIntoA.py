"""
9.1
You are given two sorted arrays, A and B, and A has a large enough buffer at the end
to hold B. Write a method to merge B into A in sorted order.
"""

def mergeTwoArrays(A,B):
    for valueB in B:
        for itr,valueA in enumerate(A):
            if valueB <= valueA:
                A.insert(itr, valueB)
                break
    return A
        
t1 = [2,4,6,8,10]
t2 = [1,3,5,7,9]

print mergeTwoArrays(t1,t2)