#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#


# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        w_list = s.split(" ")
        w_list = [w for w in w_list if w != ""]
        return len(w_list[-1])


if __name__ == "__main__":
    solution = Solution()
    solution.lengthOfLastWord("   fly me   to   the moon  ")


# @lc code=end
