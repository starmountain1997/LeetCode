#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        current_max = -1
        while left < right:
            current = (
                right-left)*(height[left] if height[left] < height[right] else height[right])
            if current > current_max:
                current_max = current
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return current_max


if __name__ == "__main__":
    s = Solution()
    s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])

        
# @lc code=end

