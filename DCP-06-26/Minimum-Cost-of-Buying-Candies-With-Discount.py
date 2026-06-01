1class Solution:
2    def minimumCost(self, cost: List[int]) -> int:
3        cost.sort(reverse=True)
4        total = 0
5        n = len(cost)
6
7        for i in range(0, n, 3):
8            total += cost[i]
9            if i + 1 < n:
10                total += cost[i + 1]
11
12        return total
13