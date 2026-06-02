1class Solution:
2    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
3        ans = float('inf')
4        n = len(landStartTime)
5        m = len(waterStartTime)
6
7        for i in range(n):
8            ls = landStartTime[i]
9            ld = landDuration[i]
10
11            for j in range(m):
12                ws = waterStartTime[j]
13                wd = waterDuration[j]
14
15                land_finish = ls + ld
16                water_start = max(land_finish, ws)
17                finish1 = water_start + wd
18
19                water_finish = ws + wd
20                land_start = max(water_finish, ls)
21                finish2 = land_start + ld
22
23                ans = min(ans, finish1, finish2)
24
25        return ans