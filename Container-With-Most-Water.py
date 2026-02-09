1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left = 0
4        right = len(height) - 1
5        max_water = 0
6
7        while left < right:
8            #Calculate current width
9            width = right - left
10            
11            # Calculate current height (limited by the shorter line)
12            current_height = min(height[left], height[right])
13            
14            # Calculate area and update max_water if current is larger
15            current_area = width * current_height
16            max_water = max(max_water, current_area)
17            
18            # Move the pointer of the shorter line inward
19            if height[left] < height[right]:
20                left += 1
21            else:
22                right -=1
23        return max_water
24        