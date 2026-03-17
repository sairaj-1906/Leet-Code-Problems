1class Solution:
2    def trap(self, height: List[int]) -> int:
3        if not height:
4            return 0
5        
6        left = 0
7        right = len(height) - 1
8
9        left_max = height[left]
10        right_max = height[right]
11
12        trapped_water = 0
13
14        while left < right:
15            # he smaller of the two max heights determines how much water can be trapped
16            if left_max < right_max:
17                left += 1
18                # Update the max height seen so far from the left
19                left_max = max(left_max, height[left])
20                # Add the trapped water at the current left pointer
21                trapped_water += left_max - height[left]
22            else:
23                right -= 1
24                # Update the max height seen so far from the right
25                right_max = max(right_max, height[right])
26                # Add the trappend water at the current right pointer
27                trapped_water += right_max - height[right]
28        
29        return trapped_water