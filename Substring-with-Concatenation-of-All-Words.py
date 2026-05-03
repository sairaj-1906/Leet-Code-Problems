1from collections import Counter
2from typing import List
3
4class Solution:
5    def findSubstring(self, s: str, words: List[str]) -> List[int]:
6        if not s or not words:
7            return []
8        
9        word_len = len(words[0])
10        num_words = len(words)
11        total_len = word_len * num_words
12        s_len = len(s)
13
14        word_counts = Counter(words)
15        ans = []
16
17        for i in range(word_len):
18            left = i
19            right = i
20            current_counts = Counter()
21            words_found = 0
22
23            while right + word_len <= s_len:
24                word = s[right:right + word_len]
25                right += word_len
26
27                if word in word_counts:
28                    current_counts[word] += 1
29                    words_found += 1
30
31                    while current_counts[word] > word_counts[word]:
32                        left_word = s[left:left + word_len]
33                        current_counts[left_word] -= 1
34                        words_found -= 1
35                        left += word_len
36                    
37                    if words_found == num_words:
38                        ans.append(left)
39                else:
40                    current_counts.clear()
41                    words_found = 0
42                    left = right
43
44        return ans