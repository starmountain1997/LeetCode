#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#


# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        for i, n in enumerate(nums[:-1]):
            if target > n and target <= nums[i + 1]:
                return i + 1
        return 0


if __name__ == "__main__":
    solution = Solution()
    solution.searchInsert([1, 3, 5, 6], 2)


# @lc code=end
