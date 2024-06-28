#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = [[root]]
        flag = False
        while len(res[-1]) != 0:
            l = []
            if flag:
                for n in res[-1][::-1]:
                    if n.left is not None:
                        l.append(n.left)
                    if n.right is not None:
                        l.append(n.right)
            else:
                for n in res[-1][::-1]:
                    if n.right is not None:
                        l.append(n.right)
                    if n.left is not None:
                        l.append(n.left)
            res.append(l)
            flag = not flag
        if len(res[-1]) == 0:
            res.pop()
        res = [[n.val for n in l] for l in res]
        return res


if __name__ == '__main__':
    s = Solution()
    s.zigzagLevelOrder(TreeNode(1, TreeNode(
        2, TreeNode(4, None, None), None), TreeNode(3, None, TreeNode(5, None, None))))

# @lc code=end
