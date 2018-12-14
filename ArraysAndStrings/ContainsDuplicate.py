# 217. Contains Duplicate (https://leetcode.com/problems/contains-duplicate/)
# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#
# Example 1:
# Input: [1,2,3,1]
# Output: true

# Example 2:
# Input: [1,2,3,4]
# Output: false

# Example 3:
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Concepts:
# - Linear Search: a method of finding if a particular value is in a list by checking each of its elements, one at a time and in sequence until the desired one is found.
# - Loop Invariant: A loop invariant is a property that holds before (and after) each iteration. Knowing its invariant(s) is essential for understanding the effect of a loop.
# -- Here is the loop invariant: Before the next search, there are no duplicate integers in the searched integers.

# Approach 1: Brute force. For each element nums[i] in nums, check if nums[j], where j < i does not equal nums[i].
# Time Complexity: O(N^2)
# Space Complexity: O(1)

# Approach 2: Sorting. Sort the list, and then sweep through the list to determine if dupes exist in sequence.
# Time Complexity: O(N * Log(N)); Comparison sorting algorithm is known to provide O(nlogn) worst-case performance. Sweeping takes O(N)
# Space Complexity: O(1)

# Approach 3: Hash Table / Set. Utilize a dynamic data structure that supports fast search and insert operations
# Reasoning: From approach 1, we realize search is O(N) in an unsorted array therefore we need a data structure with faster search
# Time Complexity: O(N)
# Space Complexity: O(N)
# Warning: Due to how hash table is designed, there may be scenarios (low N values) where Approach 3 is slower than Approach 2


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSet = set()
        for v in nums:
            if v in numSet:
                return False
            else:
                numSet.add(v)

        return True
