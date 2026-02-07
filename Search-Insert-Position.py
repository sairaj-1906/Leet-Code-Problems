1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        left = 0
4        right = len(nums) - 1
5        while left <= right:
6            #Calculate mid to avoid potential overflow in other languages
7            mid = left + (right - left) // 2
8            
9            if nums[mid] == target:
10                return mid
11            elif nums[mid] < target:
12                left = mid + 1
13            else:
14                right = mid - 1
15        #If not found, 'left' is the correct insertion index
16        return left       