#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List


class Solution:
    # TODO: 再做一遍
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res_list = []
        for i, a in enumerate(nums[:-2]):
            l = i+1
            r = len(nums)-1

            if a > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                if l > i+1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                elif r < len(nums)-1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue

                s = a+nums[l]+nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res_list.append([a, nums[l], nums[r]])
                    r -= 1
                    l += 1

        return res_list


if __name__ == "__main__":
    s = Solution()
    s.threeSum([-1, 0, 1, 2, -1, -4])
# @lc code=end
