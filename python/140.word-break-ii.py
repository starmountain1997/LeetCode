#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
from typing import List


class Solution:
    def _wordBreak(self, s: str, wordDict: List[str], res: List[str], res_list: List[List[str]]) -> List[str]:
        if len(s) == 0 and len(res) != 0:
            s = ""
            for w in res:
                s = s+w+" "
            res_list.append(s[:-1])
            return
        for i in range(len(s)+1):
            if s[:i] in wordDict:
                res.append(s[:i])
                self._wordBreak(s[i:], wordDict, res, res_list)
                res.pop()

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res_list = []
        self._wordBreak(s, wordDict, [], res_list)
        return res_list


if __name__ == "__main__":
    s = Solution()
    s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])

# @lc code=end
