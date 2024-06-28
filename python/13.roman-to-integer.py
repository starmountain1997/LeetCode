#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Intege
#


# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i, c in enumerate(s):
            if i != 0 and roman_dict[s[i - 1]] < roman_dict[c]:
                res = res - roman_dict[s[i - 1]] * 2
            res = res + roman_dict[c]
        return res


if __name__ == "__main__":
    s = Solution()
    s.romanToInt("III")


# @lc code=end
