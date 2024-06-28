#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        res = 0
        flag = True
        if x < 0:
            flag = False
            x = -x

        while x != 0:
            c = x % 10
            x = x//10
            res = res*10+c
        if res >= 0x7fffffff:  # TODO: 溢出判断
            return 0
        if flag:
            return res
        else:
            return -res


if __name__ == "__main__":
    s = Solution()
    s.reverse(1534236469)

        
# @lc code=end

