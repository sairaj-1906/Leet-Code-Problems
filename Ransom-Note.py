1from collections import Counter
2
3class Solution:
4    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
5        magazine_counts = Counter(magazine)
6
7        for char in ransomNote:
8            if magazine_counts[char] <= 0:
9                return False
10            
11            magazine_counts[char] -= 1
12        
13        return True