1class Solution:
2    def maximumJumps(self, nums: List[int], target: int) -> int:
3        n = len(nums)
4
5        dp = [-1] * n
6        dp[0] = 0
7
8        for i in range(n):
9            if dp[i] == -1:
10                continue
11            
12            for j in range(i+1, n):
13                if - target <= nums[j] - nums[i] <= target:
14                    dp[j] = max(dp[j], dp[i] + 1)
15
16        return dp[n-1]