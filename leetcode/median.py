class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1 + nums2)

        le = len(num)

        if le % 2 == 0:
            le = le // 2
            return (num[le - 1] + num[le]) / 2

        else:
            return num[le // 2] + 0.0