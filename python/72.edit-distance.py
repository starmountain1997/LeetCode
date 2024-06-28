#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # TODO: 再做一遍
        res = [[None for _ in range(len(word2)+1)]
               for _ in range(len(word1)+1)]
        for i in range(len(word2)+1):
            res[0][i] = i
        for j in range(len(word1)+1):
            res[j][0] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    res[i][j] = res[i-1][j-1]
                else:
                    res[i][j] = min(res[i-1][j], res[i][j-1], res[i-1][j-1])+1
        return res[-1][-1]


if __name__ == "__main__":
    s = Solution()
    s.minDistance("horse", "ros")

# @lc code=end
