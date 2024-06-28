#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)
            elif c == "[":
                stack.append(c)
            elif c == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(c)
            elif c == "{":
                stack.append(c)
            elif c == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    res = s.isValid("(])")
    print(res)

# @lc code=end
