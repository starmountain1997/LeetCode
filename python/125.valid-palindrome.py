import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([x for x in s.lower() if x.isalnum()])
        return s == s[::-1]


if __name__ == "__main__":
    s = Solution()
    r = s.maxProfit([7, 1, 5, 3, 6, 4])
    print(r)
