#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False]*len(s)
        for i in range(len(s)):
            tmp = ""
            for j in range(i+1):
                tmp = s[i-j]+tmp
                if tmp in wordDict:
                    if i-j == 0:
                        res[i] = True
                        break
                    elif res[i-j-1]:
                        res[i] = True
                        break

        return res[-1]


if __name__ == '__main__':
    s = Solution()
    s.wordBreak("leetcode", ["leet", "code"])

# @lc code=end
