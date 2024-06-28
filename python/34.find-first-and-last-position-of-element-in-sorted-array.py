#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def findLower(self, nums, target):
        l = 0
        r = len(nums)-1
        while l < r-1:
            m = (l+r)//2
            if nums[m] == target:
                r = m
            elif nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1

    def findUpper(self, nums, target):
        l = 0
        r = len(nums)-1
        while l < r-1:
            m = (l+r)//2
            if nums[m] == target:
                l = m
            elif nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
        if nums[r] == target:
            return r
        elif nums[l] == target:
            return l
        else:
            return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        elif len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        l = self.findLower(nums, target)
        r = self.findUpper(nums, target)
        return [l, r]


if __name__ == "__main__":
    s = Solution()
    s.searchRange([5, 7, 7, 8, 8, 10], 8)

# @lc code=end
