1from typing import List
2
3class Solution:
4    def nextPermutation(self, nums: List[int]) -> None:
5        """
6        Do not return anything, modify nums in-place instead.
7        """
8        n = len(nums)
9        i = n-2
10        while i >= 0 and nums[i] >= nums[i+1]:
11            i -= 1
12        
13        if i >= 0:
14            j = n-1
15            while nums[j] <= nums[i]:
16                j -= 1
17            nums[i], nums[j] = nums[j], nums[i]
18        
19        left, right = i+1, n-1
20        while left < right:
21            nums[left], nums[right] = nums[right], nums[left]
22            left += 1
23            right -= 1