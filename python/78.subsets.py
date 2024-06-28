#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        elif len(nums) == 1:
            return [[], [nums[0]]]
        elif len(nums) == 2:
            return [[], [nums[0]], [nums[1]], [nums[0], nums[1]]]

        res_list = self.subsets(nums[1:])
        tmp = []
        for res in res_list:
            tmp.append([nums[0]]+res)
        return res_list+tmp


if __name__ == '__main__':
    s = Solution()
    s.subsets([1, 2, 3])

# @lc code=end
