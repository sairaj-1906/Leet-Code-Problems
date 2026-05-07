1from typing import List
2
3class Solution:
4    def maxValue(self, nums: List[int]) -> List[int]:
5        n = len(nums)
6        prefix_max = [0] * n
7        prefix_max[0] = nums[0]
8        
9        for i in range(1,n):
10            prefix_max[i] = max(prefix_max[i-1], nums[i])
11
12        suffix_min = [0] * n
13        suffix_min[-1] = nums[-1]
14
15        for i in range(n-2, -1, -1):
16            suffix_min[i] = min(suffix_min[i+1], nums[i])
17        
18        ans = [0] * n
19
20        start = 0
21
22        for i in range(n-1):
23            if prefix_max[i] <= suffix_min[i+1]:
24                comp_max = max(nums[start:i+1])
25                
26                for j in range(start, i+1):
27                    ans[j] = comp_max
28
29                start = i+1
30
31        comp_max = max(nums[start:])
32
33        for j in range(start, n):
34            ans[j] = comp_max
35
36        return ans    