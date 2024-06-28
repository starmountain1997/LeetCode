#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        h = len(grid)
        w = len(grid[0])
        min_res = [[None for _ in range(w)]
                   for _ in range(h)]
        min_res[0][0] = grid[0][0]
        for i in range(1, h):
            min_res[i][0] = min_res[i-1][0]+grid[i][0]
        for j in range(1, w):
            min_res[0][j] = min_res[0][j-1]+grid[0][j]
        for i in range(1, h):
            for j in range(1, w):
                min_res[i][j] = min(
                    min_res[i-1][j], min_res[i][j-1])+grid[i][j]
        return min_res[h-1][w-1]


if __name__ == '__main__':
    s = Solution()
    s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])


# @lc code=end
