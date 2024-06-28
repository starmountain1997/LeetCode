#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sum_len = len(nums1)+len(nums2)
        if sum_len % 2 == 0:  # 偶数个
            k1 = sum_len//2-1
            k2 = sum_len//2
            res1, res2 = None, None
            p1, p2 = 0, 0
            while p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] <= nums2[p2]:
                    p1 += 1
                    if p1+p2-1 == k1:
                        res1 = nums1[p1-1]
                    elif p1+p2-1 == k2:
                        res2 = nums1[p1-1]
                        return (res1+res2)/2
                else:
                    p2 += 1
                    if p1+p2-1 == k1:
                        res1 = nums2[p2-1]
                    elif p1+p2-1 == k2:
                        res2 = nums2[p2-1]
                        return (res1+res2)/2
            while p1 < len(nums1):  # p1还没完
                p1 += 1
                if p1+p2-1 == k1:
                    res1 = nums1[p1-1]
                elif p1+p2-1 == k2:
                    res2 = nums1[p1-1]
                    return (res1+res2)/2

            while p2 < len(nums2):  # p2还没完
                p2 += 1
                if p1+p2-1 == k1:
                    res1 = nums2[p2-1]
                elif p1+p2-1 == k2:
                    res2 = nums2[p2-1]
                    return (res1+res2)/2
        else:  # 奇数个
            k = sum_len//2
            p1, p2 = 0, 0
            while p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] <= nums2[p2]:
                    p1 += 1
                    if p1+p2-1 == k:
                        return nums1[p1-1]
                else:
                    p2 += 1
                    if p1+p2-1 == k:
                        return nums2[p2-1]
            while p1 < len(nums1):  # p1还没完
                p1 += 1
                if p1+p2-1 == k:
                    return nums1[p1-1]
            while p2 < len(nums2):
                p2 += 1
                if p1+p2-1 == k:
                    return nums2[p2-1]


if __name__ == "__main__":
    s = Solution()
    s.findMedianSortedArrays([1, 2], [3,  5])

# @lc code=end
