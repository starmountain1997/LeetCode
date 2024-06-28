#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        res = [[1]*m]

        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    res.append([1])
                else:
                    res[i].append(res[i][j-1]+res[i-1][j])
        return res[n-1][m-1]


if __name__ == '__main__':
    s = Solution()
    s.uniquePaths(3, 2)

# @lc code=end
