#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        last_ptr = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last_ptr] = nums1[i]
                i -= 1
            else:
                nums1[last_ptr] = nums2[j]
                j -= 1
            last_ptr -= 1
        if j >= 0:
            nums1[0: last_ptr+1] = nums2[0: j+1]
            print(nums1)

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < m+n and j < n:
            if i >= m+j:
                nums1[i] = nums2[j]
                i += 1
                j += 1
            elif nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1[i+1:m+j+1] = nums1[i:m+j]
                nums1[i] = nums2[j]
                i += 1
                j += 1


if __name__ == "__main__":
    s = Solution()
    s.merge(nums1=[0], m=0, nums2=[1,], n=1)

# @lc code=end

