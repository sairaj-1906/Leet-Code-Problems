1import bisect
2import math
3from typing import List
4
5class Solution:
6    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
7        
8        def get_best_order_time(A_S: List[int], A_D: List[int], B_S: List[int], B_D: List[int]) -> int:
9            B = sorted(zip(B_S, B_D))
10            m = len(B)
11            B_starts = [x[0] for x in B]
12            
13            pref_min_D = [0] * m
14            pref_min_D[0] = B[0][1]
15            for i in range(1, m):
16                pref_min_D[i] = min(pref_min_D[i-1], B[i][1])
17            
18            suff_min_SD = [0] * m
19            suff_min_SD[-1] = B[-1][0] + B[-1][1]
20            for i in range(m-2, -1, -1):
21                suff_min_SD[i] = min(suff_min_SD[i+1], B[i][0] + B[i][1])
22                
23            best_time = math.inf
24            
25            for i in range(len(A_S)):
26                F_A = A_S[i] + A_D[i]
27                
28                idx = bisect.bisect_right(B_starts, F_A)
29                
30                curr_best = math.inf
31                
32                if idx > 0:
33                    curr_best = min(curr_best, F_A + pref_min_D[idx-1])
34                
35                if idx < m:
36                    curr_best = min(curr_best, suff_min_SD[idx])
37                    
38                best_time = min(best_time, curr_best)
39                
40            return best_time
41
42        return min(
43            get_best_order_time(landStartTime, landDuration, waterStartTime, waterDuration),
44            get_best_order_time(waterStartTime, waterDuration, landStartTime, landDuration)
45        )