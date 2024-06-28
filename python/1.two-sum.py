#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(nums[:-1]):
            for j, n2 in enumerate(nums[i + 1:]):
                if n1 + n2 == target:
                    return [i, j + i + 1]
        return []


if __name__ == "__main__":
    s = Solution()
    s.twoSum([3, 2, 4], 6)


# @lc code=end
