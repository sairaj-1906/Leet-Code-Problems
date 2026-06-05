1from functools import cache
2
3class Solution:
4    def totalWaviness(self, num1: int, num2: int) -> int:
5        def count_waviness(limit_str: str) -> int:
6            @cache
7            def dp(i: int, is_limit: bool, is_lead: bool, prev: int, prev_prev: int):
8               
9                if i == len(limit_str):
10                    return 0, 1 
11                
12                upper = int(limit_str[i]) if is_limit else 9
13                total_wav = 0
14                total_cnt = 0
15
16                for d in range(upper + 1):
17                    nxt_limit = is_limit and (d == upper)
18                    nxt_lead = is_lead and (d == 0)
19                    
20                    if nxt_lead:
21                        w, c = dp(i + 1, nxt_limit, True, -1, -1)
22                        total_wav += w
23                        total_cnt += c
24                    else:
25                        nxt_prev_prev = prev if not is_lead else -1
26                        w_add = 0
27                        
28                        if prev_prev != -1:
29                            if prev_prev < prev > d:
30                                w_add = 1
31                            elif prev_prev > prev < d:
32                                w_add = 1
33
34                        nxt_w, nxt_c = dp(i + 1, nxt_limit, False, d, nxt_prev_prev)
35
36                        total_wav += (nxt_w + w_add * nxt_c)
37                        total_cnt += nxt_c
38                        
39                return total_wav, total_cnt
40
41            return dp(0, True, True, -1, -1)[0]
42            
43        return count_waviness(str(num2)) - count_waviness(str(num1 - 1))