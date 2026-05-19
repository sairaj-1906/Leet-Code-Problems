1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        seen = {}
4
5        for i in range(len(nums)):
6            if nums[i] in seen and i - seen[nums[i]] <= k:
7                return True
8            
9            seen[nums[i]] = i
10        
11        return False