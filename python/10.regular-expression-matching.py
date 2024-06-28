#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:  # s[i]和p[j]match
            return len(s) == 0
        m = [[None for _ in range(len(p))] for _ in range(len(s))]
        i, j = 0, 0
        while i < len(s) and j < len(p):
            if p[j] == ".":
                m[i][j] = m[i-1][j-1] and p[j-1] == s[i]
                j += 1
                i += 1
            elif p[j] == "*":
                m[i][j] = m[i][j-1] and p[j-1] == s[i]
                i += 1
            else:
                m[i][j] = p[j] == s[i]
                i += 1
                j += 1

        return m[-1][-1]


if __name__ == "__main__":
    s = Solution()
    s.isMatch("aaa", "a*")

# @lc code=end
