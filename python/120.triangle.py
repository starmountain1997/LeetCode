#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0
        elif len(triangle) == 1:
            return triangle[0][0]

        min_res = [[triangle[0][0]]]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:  # 第一个
                    min_res.append([triangle[i][j]+min_res[i-1][j]])
                elif j == len(triangle[i])-1:  # 倒数第一个
                    min_res[i].append(triangle[i][j]+min_res[i-1][j-1])
                else:
                    this_min = min(min_res[i-1][j], min_res[i-1][j-1])
                    min_res[i].append(this_min+triangle[i][j])
        return min(min_res[-1])


if __name__ == '__main__':
    s = Solution()
    s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])


# @lc code=end
