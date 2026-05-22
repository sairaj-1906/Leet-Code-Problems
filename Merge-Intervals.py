1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort(key=lambda x: x[0])
4
5        merged = []
6
7        for interval in intervals:
8            if not merged or merged[-1][1] < interval[0]:
9                merged.append(interval)
10            else:
11                merged[-1][1] = max(merged[-1][1], interval[1])
12
13        return merged
14