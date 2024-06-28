#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[None for _ in range(n)] for _ in range(n)]
        h = [0, n]
        w = [0, n]
        d = 0  # 方向
        for n in range(1, n*n+1):
            for i in range(1, n):
                for j in range(1, n):
                    res[i][j] = n
        return res


if __name__ == '__main__':
    s = Solution()
    s.generateMatrix(3)

# @lc code=end
