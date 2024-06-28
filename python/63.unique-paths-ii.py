#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])
        res = [[0 for _ in range(w)] for _ in range(h)]
        res[0][0] = 1
        for i in range(h):
            for j in range(w):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    continue
                a = res[i][j-1] if j >= 1 and obstacleGrid[i][j-1] == 0 else 0
                b = res[i-1][j] if i >= 1 and obstacleGrid[i-1][j] == 0 else 0
                res[i][j] = a+b
        return res[-1][-1]


if __name__ == "__main__":
    s = Solution()
    s.uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]])

# @lc code=end
