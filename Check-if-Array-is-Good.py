1class Solution:
2    def isGood(self, nums: List[int]) -> bool:
3        n = max(nums)
4
5        if len(nums) != n+1:
6            return False
7        
8        count = [0] * (n+1)
9        for num in nums:
10            if num > n:
11                return False
12            count[num] += 1
13
14        for i in range(1, n):
15            if count[i] != 1:
16                return False
17        
18        return count[n] == 2