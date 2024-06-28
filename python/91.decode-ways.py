#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == "0":
            return 0
        res = [0 for _ in range(len(s))]
        res[0] = 1
        for i, c in enumerate(s[1:]):
            if c != "0":
                res[i+1] = res[i]
        return res[-1]


if __name__ == "__main__":
    s = Solution()
    b = s.numDecodings("123123")  # 9

# @lc code=end
