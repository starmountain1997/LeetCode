#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#


# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow_p = -1
        fast_p = 0
        while fast_p < len(nums):
            if nums[fast_p] == val:
                fast_p = fast_p + 1
            else:
                nums[slow_p + 1] = nums[fast_p]
                slow_p = slow_p + 1
                fast_p = fast_p + 1
        return slow_p + 1


if __name__ == "__main__":
    solution = Solution()
    solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)


# @lc code=end
