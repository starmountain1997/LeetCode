#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List


class Solution:
    def _generateParenthesis(self,  left: int, right: int, res: str, res_list: List[str]) -> List[str]:
        if left == 0 and right == 0:
            res_list.append(res)
            return
        if left > right:
            return
        if left > 0:
            self._generateParenthesis(left-1, right, res+"(", res_list)
        if right > 0:
            self._generateParenthesis(left, right-1, res+")", res_list)

    def generateParenthesis(self, n: int) -> List[str]:
        res_list = []
        self._generateParenthesis(n, n, "", res_list)
        return res_list


if __name__ == "__main__":
    s = Solution()
    s.generateParenthesis(2)

# @lc code=end
