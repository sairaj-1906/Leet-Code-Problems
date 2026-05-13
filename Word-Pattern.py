1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        words = s.split()
4
5        if len(pattern) != len(words):
6            return False
7        
8        char_to_word = {}
9        word_to_char = {}
10
11        for ch, word in zip(pattern, words):
12            if ch in char_to_word:
13                if char_to_word[ch] != word:
14                    return False
15            else:
16                char_to_word[ch] = word
17
18            if word in word_to_char:
19                if word_to_char[word] != ch:
20                    return False
21            else:
22                word_to_char[word] = ch
23        
24        return True