1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left, right = 0, len(nums) - 1
4
5        while left <= right:
6            mid = left + right
7
8            if nums[mid] == target:
9                return mid
10
11            if nums[left] <= nums[mid]:
12                if nums[left] <= target < nums[mid]:
13                    right = mid - 1
14                else:
15                    left = mid + 1
16
17            else:
18                if nums[mid] < target <= nums[right]:
19                    left = mid + 1
20                else:
21                    right = mid - 1
22
23        return -1
24