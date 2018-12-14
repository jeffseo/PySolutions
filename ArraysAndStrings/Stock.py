# 121. Best Time to Buy and Sell Stock (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# Solution: We need to find out the maximum difference (which will be the maximum profit) between two numbers in the given array. Also, the second number (selling price) must be larger than the first one (buying price).
# formal terms, need to find max(prices[j], prices[i]) for every i and j such that j > i

# Approach 1: Brute Force: For each stock value v in array, calculate and store the max value gained when sold in the later day i.
# Complexity:
# - Time: O(N^2); Loop runs n * (n - 1) / 2
# - Space: O(1); Two variables, max profit and profit

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#
#         maxProfit = 0
#
#         for i, buyValue in enumerate(prices[:-1]):
#             for sellValue in prices[i + 1:]:
#                 profit = sellValue - buyValue
#                 if profit > maxProfit:
#                     maxProfit = profit
#
#         return maxProfit

# Approach 2: One pass
# We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.
# Complexity Analysis:
# Time complexity : O(N) Only a single pass is needed.
# Space complexity : O(1) Only two variables are used

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        buyPrice = sys.maxsize

        for price in prices:
            if price < buyPrice:
                buyPrice = price
            else:
                profit = price - buyPrice
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit
