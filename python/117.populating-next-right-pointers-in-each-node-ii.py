#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if root is None:
            return
        res = [[root]]
        while len(res[-1]) != 0:
            l = []
            for n in res[-1]:
                if n.left:
                    l.append(n.left)
                if n.right:
                    l.append(n.right)
            res.append(l)
        if len(res) == 0:
            res.pop()
        for l in res:
            for n, r in zip(l[:-1], l[1:]):
                n.next = r
        return root

# @lc code=end
