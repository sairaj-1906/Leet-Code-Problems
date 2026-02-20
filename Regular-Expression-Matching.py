1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        memo = {}
4
5        def dfs(i , j):
6            # If we already computed this state, return the cached result
7            if (i, j) in memo:
8                return memo[(i, j)]
9            
10            # Base case: if we reach the end of the pattern
11            if j == len (p):
12                return i == len(s)
13            
14            # Check if current characters match (accounting for '.')
15            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
16
17            # If the next character in pattern is '*'
18            if j + 1 < len(p) and p[j + 1] == '*':
19                # Branch 1: Skip the preceding element and the '*' (zero occurrences)
20                # Branch 2: Current character matches, keep the '*' to match the next character in 's'
21                ans = dfs(i, j + 2) or (match and dfs (i + 1, j))
22            else:
23                # Normal character match, advance both pointers
24                ans = match and dfs(i + 1, j + 1)
25                ans = match and dfs(i + 1, j + 1)
26            
27            # Cache and return the result
28            memo[(i, j)] = ans
29            return ans
30        
31        # Start matching from the beginning of both strings
32        return dfs(0, 0)