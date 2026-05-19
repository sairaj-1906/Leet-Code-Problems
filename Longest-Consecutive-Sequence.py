1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        num_set = set(nums)
4        longest = 0
5
6        for num in num_set:
7            if num - 1 not in num_set:
8                current = num
9                length = 1
10
11                while current + 1 in num_set:
12                    current += 1
13                    length += 1
14                
15                longest = max(longest, length)
16        
17        return longest