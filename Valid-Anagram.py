1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5
6        count = {}
7
8        for ch in s:
9            count[ch] = count.get(ch, 0) + 1
10
11        for ch in t:
12            if ch not in count:
13                return False
14            
15            count[ch] -= 1
16
17            if count[ch] < 0:
18                return False
19        
20        return True