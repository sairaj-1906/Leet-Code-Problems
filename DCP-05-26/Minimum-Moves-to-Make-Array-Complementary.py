1class Solution:
2    def minMoves(self, nums: List[int], limit: int) -> int:
3        n = len(nums)
4
5        diff = [0] * (2 * limit + 2)
6
7        left = 0
8        right = n-1
9
10        while left < right:
11            a = nums[left]
12            b = nums[right]
13
14            low = min(a, b) + 1
15            high = max(a, b) + limit
16            total = a + b
17
18            diff[2] += 2
19
20            diff[low] -= 1
21            diff[high + 1] += 1
22
23            diff[total] -= 1
24            diff[total + 1] += 1
25
26            left += 1
27            right -= 1
28        
29        ans = float('inf')
30        current = 0
31
32        for s in range(2, 2 * limit + 1):
33            current += diff[s]
34            ans = min(ans, current)
35
36        return ans