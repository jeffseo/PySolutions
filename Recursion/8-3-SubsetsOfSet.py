"""
8.3
Write a method that returns all subsets of a set.

http://stackoverflow.com/questions/4640034/calculating-all-of-the-subsets-of-a-set-of-numbers
Approach 1
1. Take the first element of your number list
2. generate all subsets from the remaining number list (i.e. the number list without the chosen one) => Recursion!
3. for every subset found in the previous step, add the subset itself and the subset joined with the element chosen in step 1 to the output.

Of course, you have to check the base case, i.e. if your number list is empty.

Approach 2
It is a well known fact that a set with n elements has 2^n subsets. 
Thus, you can count in binary from 0 to 2^n and interpret the binary number as the corresponding subset. 
Note that this approach requires a binary number with a sufficient amount of digits to represent the whole set.
"""

def getSubsets(ogSet):
    if len(ogSet) == 0:
        return ogSet
    totalSet = []
    head = ogSet.pop(0)
    rest = list(ogSet)
    subSets = getSubsets(rest)
    for sets in subSets:
        newSet = [head] + sets
        totalSet.append(newSet)
        totalSet.append(sets)
    return totalSet

# https://www.quora.com/What-is-the-recursive-solution-for-finding-all-subsets-of-a-given-array
def getSubsets_iterative(nums):
    if nums is None:
        return None
    subsets = [[]] 
    for n in nums:
        temp = []
        for s in subsets:
            temp.append(s + [n])
        subsets += temp
        #print subsets
    return subsets 

print getSubsets_iterative([1,2,3])
print getSubsets([1,2,3])