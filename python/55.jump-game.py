#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # TODO: 再做一遍
        max_reach = 0
        for i, n in enumerate(nums):
            if i > max_reach or max_reach > len(nums):
                break
            max_reach = max(max_reach, i+n)
        return max_reach >= len(nums)-1


if __name__ == "__main__":
    s = Solution()
    s.canJump([0, ])

# @lc code=end
