#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        d = 0  # 0右,1下,2左,3上
        h = [0, len(matrix)]
        w = [0, len(matrix[0])]
        res = []
        while h[0] != h[1] and w[0] != w[1]:
            if d == 0:
                for i in range(w[0], w[1]):
                    res.append(matrix[h[0]][i])
                h[0] += 1
            elif d == 1:
                for i in range(h[0], h[1]):
                    res.append(matrix[i][w[1]-1])
                w[1] -= 1
            elif d == 2:
                for i in range(w[1]-1, w[0]-1, -1):
                    res.append(matrix[h[1]-1][i])
                h[1] -= 1
            elif d == 3:
                for i in range(h[1]-1, h[0]-1, -1):
                    res.append(matrix[i][w[0]])
                w[0] += 1
            d = (d+1) % 4
        return res


if __name__ == '__main__':
    s = Solution()
    s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# @lc code=end
