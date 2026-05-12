1from typing import List
2
3class Solution:
4    def minimumEffort(self, tasks: List[List[int]]) -> int:
5        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
6
7        ans = 0
8        curr = 0
9
10        for actual, minimum in tasks:
11            if curr < minimum:
12                ans += (minimum - curr)
13                curr = minimum
14            
15            curr -= actual
16        
17        return ans