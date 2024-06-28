#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        str = str.strip()
        if len(str) == 0:
            return 0

        sign = 1
        val = 0
        if str[0] in ["-", "+"]:
            sign = 1 if str[0] == '+' else -1
            str = str[1:]

        for char in str:
            if not char.isdigit():
                break
            val = val * 10 + (ord(char) - ord("0"))

        return min(INT_MAX, max(INT_MIN, val * sign))


# @lc code=end
