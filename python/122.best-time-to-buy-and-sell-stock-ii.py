#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        res = 0
        for pi, pi_1 in zip(prices[:-1], prices[1:]):
            if pi_1 > pi:
                res += pi_1 - pi
        return res


if __name__ == '__main__':
    s = Solution()
    s.maxProfit([7, 1, 5, 3, 6, 4])

# @lc code=end
