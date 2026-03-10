1from typing import List
2
3class Solution:
4    def canJump(self, nums: List[int]) -> bool:
5        max_reach = 0
6        target = len(nums) - 1
7
8        for i, jump in enumerate(nums):
9            # If the current index is beyond our furthest reach, we are stuck
10            if i > max_reach:
11                return False
12            
13            # Update the furthest index we can reach
14            max_reach = max(max_reach, i + jump)
15
16            # If our reach extends to or beyond the last index, we're done
17            if max_reach >= target:
18                return True
19        return True