1from collections import Counter
2
3class Solution:
4    def minWindow(self, s: str, t: str) -> str:
5        
6        if len(t) > len(s):
7            return ""
8
9        need = Counter(t)
10        window = {}
11
12        have = 0
13        required = len(need)
14
15        left = 0
16        min_len = float('inf')
17        result = [-1, -1]
18
19        for right in range(len(s)):
20            char = s[right]
21
22            window[char] = window.get(char, 0) + 1
23
24            # Check if current char satisfies requirement
25            if char in need and window[char] == need[char]:
26                have += 1
27
28            # Shrink window
29            while have == required:
30
31                # Update answer
32                window_size = right - left + 1
33                if window_size < min_len:
34                    min_len = window_size
35                    result = [left, right]
36
37                # Remove left character
38                left_char = s[left]
39                window[left_char] -= 1
40
41                if left_char in need and window[left_char] < need[left_char]:
42                    have -= 1
43
44                left += 1
45
46        l, r = result
47
48        return s[l:r+1] if min_len != float('inf') else ""