1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        # If the array has only 1 element, we're already at the end
4        if len(nums) <= 1:
5            return 0
6        
7        jumps = 0
8        current_end = 0
9        farthest = 0
10
11        # We don't need to iterate the last element because 
12        # we are guaranteed to reach it.
13        for i in range(len(nums) - 1):
14            # Update the farthest index we can reach from the current position
15            farthest = max(farthest, i + nums[i])
16
17            # If we've reached the end of the current jump's range
18            if i == current_end:
19                jumps += 1
20                current_end = farthest
21
22                # Early exit optimization:
23                # If our current range already reaches or exceeds the last index, we can stop
24                if current_end >= len(nums) - 1:
25                    break
26        
27        return jumps