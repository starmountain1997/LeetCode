#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # TODO: 再做一遍
        h = len(matrix)
        w = len(matrix[0])
        l = 0
        r = h*w  # 这里不用-1
        while l < r:
            m = (l+r)//2
            x = m//w
            y = m % w
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = m+1
            elif matrix[x][y] > target:
                r = m
        return False


if __name__ == '__main__':
    s = Solution()
    s.searchMatrix([
        [1,   3,  5,  7],
        [10,   11,  16,  20],
        [23,   30,  34,  60],
    ], 13)
# @lc code=end
