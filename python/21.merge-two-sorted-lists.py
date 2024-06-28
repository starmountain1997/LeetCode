#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 把list2插到list1里面去
        if not list1 and not list2:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        i = list1
        j = list2
        while i.next and j:
            if i.next.val > j.val:
                tmp1, tmp2 = i.next, j.next
                i.next = j
                j.next = tmp1
                j = tmp2
            else:
                i = i.next
        if j:
            i.next = j
        return list1


if __name__ == "__main__":
    l1 = ListNode(1, None)
    l2 = ListNode(2, None)
    l3 = ListNode(4, None)
    l4 = ListNode(1, None)
    l5 = ListNode(3, None)
    l6 = ListNode(4, None)
    l1.next = l2
    l2.next = l3
    l4.next = l5
    l5.next = l6

    sol = Solution()
    sol.mergeTwoLists(list1=l1, list2=l4)


# @lc code=end
