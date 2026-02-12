1from typing import List
2
3class Solution:
4    def threeSum(self, nums: List[int]) -> List[List[int]]:
5        nums.sort()  # Sort the array first
6        n = len(nums)
7        result = []
8        
9        for i in range(n - 2):
10            # Optimization: If the current number is > 0, the sum can't be 0 
11            # because the array is sorted and subsequent numbers are also positive.
12            if nums[i] > 0:
13                break
14                
15            # Skip duplicate elements for the first position of the triplet
16            if i > 0 and nums[i] == nums[i - 1]:
17                continue
18            
19            # Two-pointer approach
20            left, right = i + 1, n - 1
21            while left < right:
22                total = nums[i] + nums[left] + nums[right]
23                
24                if total < 0:
25                    left += 1
26                elif total > 0:
27                    right -= 1
28                else:
29                    # Found a triplet
30                    result.append([nums[i], nums[left], nums[right]])
31                    
32                    # Skip duplicate elements for the second position
33                    while left < right and nums[left] == nums[left + 1]:
34                        left += 1
35                    # Skip duplicate elements for the third position
36                    while left < right and nums[right] == nums[right - 1]:
37                        right -= 1
38                    
39                    # Move pointers inward after processing duplicates
40                    left += 1
41                    right -= 1
42                    
43        return result