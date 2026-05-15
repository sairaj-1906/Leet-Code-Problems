1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left = 0
4        right = len(nums) - 1
5
6        while left < right:
7            mid = (left + right) // 2
8
9            if nums[mid] > nums[right]:
10                left = mid + 1
11            else:
12                right = mid
13        
14        return nums[left]