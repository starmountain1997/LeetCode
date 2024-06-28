#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        res = 0
        for i, a in enumerate(nums[:-2]):
            l = i+1
            r = len(nums)-1
            while l < r:
                s = a+nums[l]+nums[r]
                if s > target:
                    d = s-target
                    if d < closest:
                        closest = d
                        res = s
                    r -= 1
                elif s < target:
                    d = target-s
                    if d < closest:
                        closest = d
                        res = s
                    l += 1
                else:
                    return target
        return res


if __name__ == "__main__":
    s = Solution()
    s.threeSumClosest([-1, 2, 1, -4], 1)
# @lc code=end
