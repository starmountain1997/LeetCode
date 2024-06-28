#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#


# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        f = 0
        x = str(x)
        e = len(x) - 1
        for i in range(len(x) // 2):
            if x[f + i] != x[e - i]:
                return False
        return True


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    s.isPalindrome(12)
