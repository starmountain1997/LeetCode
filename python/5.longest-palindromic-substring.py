#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ref: https://writings.sh/post/algorithm-longest-palindromic-substring
        # TODO: 优化
        if len(s) <= 1:
            return s
        # dp[i][j] 表示 s[i...j] 是否为回文串
        dp = [[None for _ in range(len(s))]for _ in range(len(s))]
        max_length = 1
        res = s[0]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = s[i] == s[j]
                    if max_length <= 1 and dp[i][j]:
                        res = s[i:j+1]
                        l = 2
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
                        if dp[i][j]:
                            if j-i+1 > max_length:
                                max_length = j-i+1
                                res = s[i:j+1]
                    else:
                        dp[i][j] = False
        return res


if __name__ == '__main__':
    s = Solution()
    s.longestPalindrome('aaaa')

# @lc code=end
