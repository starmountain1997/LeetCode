#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if nums[m] < nums[r]:  # 这样判断可以处理[3, 1]找1的情况
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            else:  # 右半边是有序的
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
        return -1


if __name__ == "__main__":
    s = Solution()
    s.search([3, 1], 1)
# @lc code=end
