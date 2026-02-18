1from typing import List
2class Solution:
3    def threeSumClosest(self, nums: List[int], target: int) -> int:
4        nums.sort()
5        n = len(nums)
6        closest_sum = float('inf')
7
8        for i in range(n - 2):
9            left, right = i + 1, n - 1
10
11            while left < right:
12                current_sum = nums[i] + nums[left] +nums[right]
13                
14                # Update closest_sum if current is closer to target
15
16                if abs(current_sum - target) < abs(closest_sum - target):
17                    closest_sum = current_sum
18                
19                if current_sum < target:
20                    left += 1
21                elif current_sum > target:
22                    right -= 1
23                else:
24                    return target       # Exact match found
25        
26        return closest_sum
27