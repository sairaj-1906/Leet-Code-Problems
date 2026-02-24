1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n <= 2:
4            return n
5        prev, curr = 1, 2       # ways to reach step 1 and step 2
6
7        for _ in range(3, n + 1):
8            prev, curr = curr, prev + curr
9        return curr