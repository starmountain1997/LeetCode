#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_price = prices[0]
        res = float('-inf')
        for p in prices[1:]:
            this_profit = p - min_price
            if this_profit > res:
                res = this_profit
            min_price = min(p, min_price)
        return max(res, 0)


if __name__ == '__main__':
    s = Solution()
    s.maxProfit([7, 1, 5, 3, 6, 4])

# @lc code=end
