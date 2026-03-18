1class Solution:
2    def reverseWords(self, s: str) -> str:
3        words = []
4        word = ""
5
6        for ch in s:
7            if ch != ' ':
8                word += ch
9            elif word:
10                words.append(word)
11                word = ""
12        
13        if word:
14            words.append(word)
15
16        return " ".join(words[::-1])