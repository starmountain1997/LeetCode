#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res_list = []
        for i, a in enumerate(nums[:-3]):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j+1
                r = len(nums)-1
                while l < r:
                    if l > j+1 and nums[l] == nums[l-1]:
                        l += 1
                        continue
                    elif r < len(nums)-1 and nums[r] == nums[r+1]:
                        r -= 1
                        continue

                    s = a+nums[j]+nums[l]+nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res_list.append([a, nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

        return res_list


if __name__ == "__main__":
    s = Solution()
    s.fourSum([-1, 0, 1, 2, -1, -4], -1)

# @lc code=end
