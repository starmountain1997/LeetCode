#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = 0
        if len(strs) == 0:
            return ""
        for cs in zip(*strs):
            cs = set(cs)
            if len(cs) == 1:
                res = res + 1
            else:
                break
        return strs[0][:res]


if __name__ == "__main__":
    s = Solution()
    r = s.longestCommonPrefix(["flower", "flow", "flight"])
    print(r)


# @lc code=end
