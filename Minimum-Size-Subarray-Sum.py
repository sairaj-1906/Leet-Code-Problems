1from typing import List
2
3class Solution:
4    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
5        left = 0
6        current_sum = 0
7        min_length = float('inf')
8
9        for right in range(len(nums)):
10            current_sum += nums[right]
11
12            while current_sum >= target:
13                min_length = min(min_length, right - left + 1)
14                current_sum -= nums[left]
15                left += 1
16        
17        return 0 if min_length == float('inf') else min_length