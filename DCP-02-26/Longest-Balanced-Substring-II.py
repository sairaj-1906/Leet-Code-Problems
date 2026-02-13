1class Solution:
2    def longestBalanced(self, s: str) -> int:
3        n = len(s)
4        max_len = 0
5    
6        # --- Case 1: Substrings with 1 distinct character ---
7        # We simply look for the longest run of identical characters.
8        i = 0
9        while i < n:
10            start = i
11            while i < n and s[i] == s[start]:
12                i += 1
13            max_len = max(max_len, i - start)
14        
15        # --- Case 2: Substrings with 2 distinct characters ---
16        # Helper to find longest balanced substring using only char1 and char2.
17        # The third character acts as a strict boundary (reset).
18        def solve_two_chars(c1, c2):
19            res = 0
20            balance = 0
21            # Map balance value to its first occurrence index.
22            # Initialize with 0 balance at index -1.
23            seen = {0: -1}
24        
25            for i, char in enumerate(s):
26                if char == c1:
27                    balance += 1
28                elif char == c2:
29                    balance -= 1
30                else:
31                    # If we see the 3rd char, the substring breaks. Reset.
32                    seen = {0: i}
33                    balance = 0
34                    continue
35            
36                if balance in seen:
37                    res = max(res, i - seen[balance])
38                else:
39                    seen[balance] = i
40            return res
41
42        max_len = max(max_len, solve_two_chars('a', 'b'))
43        max_len = max(max_len, solve_two_chars('b', 'c'))
44        max_len = max(max_len, solve_two_chars('a', 'c'))
45
46        # --- Case 3: Substrings with 3 distinct characters ---
47        # We want a substring where count(a) == count(b) == count(c).
48        # This implies: (count(a) - count(b)) is constant AND (count(b) - count(c)) is constant.
49        seen = {(0, 0): -1}
50        cnt = {'a': 0, 'b': 0, 'c': 0}
51    
52        for i, char in enumerate(s):
53            cnt[char] += 1
54        
55            # The state is defined by the relative differences between counts
56            diff1 = cnt['a'] - cnt['b']
57            diff2 = cnt['b'] - cnt['c']
58            state = (diff1, diff2)
59        
60            if state in seen:
61                max_len = max(max_len, i - seen[state])
62            else:
63                seen[state] = i
64            
65        return max_len
66        