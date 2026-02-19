1class Solution:
2    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
3        nums.sort()
4        n = len(nums)
5        res = []
6        
7        # Outer loop to fix the first number
8        for i in range(n - 3):
9            # Skip duplicates for the first number
10            if i > 0 and nums[i] == nums[i - 1]:
11                continue
12            
13            # Pruning: The smallest sum is too large, stop checking further 'i's
14            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
15                break
16            # Pruning: The largest sum is too small, move to the next 'i'
17            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
18                continue
19                
20            # Inner loop to fix the second number
21            for j in range(i + 1, n - 2):
22                # Skip duplicates for the second number
23                if j > i + 1 and nums[j] == nums[j - 1]:
24                    continue
25                
26                # Pruning for 'j'
27                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
28                    break
29                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
30                    continue
31                
32                # Two pointers for the third and fourth numbers
33                left, right = j + 1, n - 1
34                
35                while left < right:
36                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
37                    
38                    if curr_sum == target:
39                        res.append([nums[i], nums[j], nums[left], nums[right]])
40                        left += 1
41                        right -= 1
42                        
43                        # Skip duplicates for the third and fourth numbers
44                        while left < right and nums[left] == nums[left - 1]:
45                            left += 1
46                        while left < right and nums[right] == nums[right + 1]:
47                            right -= 1
48                            
49                    elif curr_sum < target:
50                        left += 1
51                    else:
52                        right -= 1
53                        
54        return res