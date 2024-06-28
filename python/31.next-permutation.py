#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List


class Solution:
    # TODO: 再做一遍
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                min = nums[i]
                k = i
                for j in range(i, len(nums)):
                    if nums[i-1] < nums[j] < min:
                        min = nums[j]
                        k = j

                nums[i-1], nums[k] = nums[k], nums[i-1]
                nums[i:] = sorted(nums[i:])
                return
        nums.sort()  # 返回升序排列


if __name__ == "__main__":
    s = Solution()
    s.nextPermutation([1, 3, 2])

# @lc code=end
