#
# @lc app=leetcode id=28 lang=python
#
# [28] Find the Index of the First Occurrence in a String
#


# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        len_needle = len(needle)
        while i + len_needle <= len(haystack):
            if haystack[i : i + len(needle)] == needle:
                return i
            i = i + 1

        return -1
if __name__ == "__main__":
    solution = Solution()
    solution.strStr("a", "a")

# @lc code=end
