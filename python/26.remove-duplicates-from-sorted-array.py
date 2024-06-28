#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow_p = 0
        fast_p = 1
        while fast_p < len(nums):
            if nums[slow_p] == nums[fast_p]:
                fast_p = fast_p + 1
            else:
                nums[slow_p + 1] = nums[fast_p]
                slow_p = slow_p + 1
                fast_p = fast_p + 1
        return slow_p + 1


if __name__ == "__main__":
    solution = Solution()
    solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])


# @lc code=end
