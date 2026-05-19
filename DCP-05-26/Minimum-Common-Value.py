1class Solution:
2    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
3        i, j = 0, 0
4
5        while i < len(nums1) and j < len(nums2):
6            if nums1[i] == nums2[j]:
7                return nums1[i]
8            elif nums1[i] < nums2[j]:
9                i += 1
10            else:
11                j += 1
12        
13        return -1