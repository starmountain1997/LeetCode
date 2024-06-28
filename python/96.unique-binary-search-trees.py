#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
from typing import Dict


class Solution:

    def _numTrees(self, n: int, d: Dict) -> int:
        if n in d:
            return d[n]
        res = 0
        for i in range(n):
            if i in d:
                left = d[i]
            else:
                left = self._numTrees(i, d)
            if (n-i-1) in d:
                right = d[n-i-1]
            else:
                right = self._numTrees(n-i-1, d)
            res = res+left*right
        d[n] = res
        return res

    def numTrees(self, n: int) -> int:
        res = self._numTrees(n, {0: 1, 1: 1, 2: 2})
        return res


if __name__ == "__main__":
    solution = Solution()
    res = solution.numTrees(19)
    print(res)

# @lc code=end

