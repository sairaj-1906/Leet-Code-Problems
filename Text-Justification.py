1class Solution:
2    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
3        res = []
4        i = 0
5        n = len(words)
6        
7        while i<n:
8            line_len = len(words[i])
9            j = i+1
10
11            while j<n and line_len + 1 + len(words[j]) <= maxWidth:
12                line_len += 1 + len(words[j])
13                j += 1
14            
15            line_words = words[i:j]
16            num_words = j-i
17            total_chars = sum(len(word) for word in line_words)
18
19            spaces = maxWidth - total_chars
20
21            if j == n or num_words == 1:
22                line = " ".join(line_words)
23                line += " " * (maxWidth - len(line))
24            else:
25                gaps = num_words - 1
26                space_per_gap = spaces // gaps
27                extra_spaces = spaces % gaps
28
29                line = ""
30                for k in range(gaps):
31                    line += line_words[k]
32                    line += " " * (space_per_gap + (1 if k < extra_spaces else 0))
33                line += line_words[-1]
34            
35            res.append(line)
36            i = j
37
38        return res