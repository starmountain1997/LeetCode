#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # TODO: 再做一遍
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        ms = [nums[0]]  # 以i结尾的最大子数组和
        max = nums[0]
        for i in range(1, len(nums)):
            s = ms[i-1]+nums[i]
            if s > nums[i]:
                ms.append(s)
            else:
                ms.append(nums[i])
            if ms[i] > max:
                max = ms[i]
        return max


if __name__ == '__main__':
    s = Solution()
    res = s.maxSubArray([-1, -2])
    print(res)

# @lc code=end
