#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        p = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b = p.pop()
                a = p.pop()
                if token == "+":
                    c = a+b
                elif token == "-":
                    c = a-b
                elif token == "*":
                    c = a*b
                elif token == "/":
                    c = a/b
                p.append(math.trunc(c))  # TODO: 使用trunc
            else:
                p.append(int(token))
        return p[-1]


if __name__ == '__main__':
    s = Solution()
    s.evalRPN(["4", "13", "5", "/", "+"])

# @lc code=end
