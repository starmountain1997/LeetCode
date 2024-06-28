#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        d = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }
        res = [""]
        for c in digits:
            this_d = d[c]
            res = [n+k for k in this_d for n in res]
        return res


if __name__ == "__main__":
    s = Solution()
    s.letterCombinations("23")

# @lc code=end
