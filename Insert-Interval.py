1from typing import List
2
3class Solution:
4    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
5        result = []
6        i = 0
7        n = len(intervals)
8
9        while i<n and intervals[i][1] < newInterval[0]:
10            result.append(intervals[i])
11            i += 1
12        
13        while i<n and intervals[i][0] <= newInterval[1]:
14            newInterval[0] = min(newInterval[0], intervals[i][0])
15            newInterval[1] = max(newInterval[1], intervals[i][1])
16            i += 1
17        
18        result.append(newInterval)
19
20        while i<n :
21            result.append(intervals[i])
22            i += 1
23        
24        return result