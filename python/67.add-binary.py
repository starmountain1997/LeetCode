#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        res = ""
        if len(b) > len(a):
            a, b = b, a
        b = b.zfill(len(a))  # 给b补0
        for ac, bc in zip(a[::-1], b[::-1]):
            o = int(ac)+int(bc)+c
            if o == 0 or o == 1:
                c = 0
            elif o == 2:
                c = 1
                o = 0
            elif o == 3:
                c = 1
                o = 1
            res = str(o)+res
        if c == 1:
            res = "1"+res
        res = str(int(res))
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.addBinary("11", "1")
    print(res)
# @lc code=end
