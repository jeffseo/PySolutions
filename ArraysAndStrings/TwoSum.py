# https://medium.freecodecamp.org/coding-interviews-for-dummies-5e048933b82b
# 1. Two Sum (https://leetcode.com/problems/two-sum/)
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Approach 1: Brute Force
# - Loop through each element x and find if there another value that equals target - x
# - Complexity:
# -- Time: O(n^2). For each element, we try to find its complement by looping through rest of the array which takes O(n).
# -- Space: O(1).

# Approach 2: Two-pass
# - Need a quick way to check if a complement exists in the array and if so, get its index. The best way to maintain a mapping of each element in the array to its index? Hash table.
# - Two iteration: first iteration to add each elements index and its value to the table. Then, we check each value's complement exists in the table. The complement must not be the value itself!
# - Complexity:
# -- Time: O(n); traverse n elements exactly twice. since hash table lookup is O(1), time complexity is O(n)
# -- Space: O(n); Extra space is needed to store the elements from the list into hash table.
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         numDict = {}
#         for i, key in enumerate(nums):
#             if (key in numDict) == False:
#                 numDict[key] = []
#             numDict[key].append(i)
#
#         for i, key in enumerate(nums):
#             diff = target - key
#             if diff in numDict:
#                 for j in numDict[diff]:
#                     if j != i:
#                         return [i, j]
        #
        # return -1

# Approach 3: Single-pass
# - It turns out we can do it in one-pass. While we iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table.
# - If it exists, we have found a solution and return immediately.
# - Complexity:
# -- Time: O(n); traverse n elements exactly once. since hash table lookup is O(1), time complexity is O(n)
# -- Space: O(n); Extra space is needed to store the elements from the list into hash table.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        for i, key in enumerate(nums):
            if (key in numDict) == False:
                numDict[key] = i

            diff = target - key
            if diff in numDict and numDict[diff] != i:
                return [i, numDict[diff]]

        return -1
