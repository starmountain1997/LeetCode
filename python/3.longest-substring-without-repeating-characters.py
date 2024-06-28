#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_length = 0
        first_appear_dict = dict()
        for right, c in enumerate(s):
            if c not in first_appear_dict.keys():
                first_appear_dict[c] = right
                this_length = right-left+1
                max_length = max_length if max_length > this_length else this_length
            else:
                if left < first_appear_dict[c]+1:
                    left = first_appear_dict[c]+1
                this_length = right-left+1
                max_length = max_length if max_length > this_length else this_length
                first_appear_dict[c] = right
        return max_length


if __name__ == "__main__":
    s = Solution()
    res = s.lengthOfLongestSubstring("abba")
    print(res)


# @lc code=end
