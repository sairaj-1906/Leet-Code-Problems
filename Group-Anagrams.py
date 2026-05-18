1from typing import List
2from collections import defaultdict
3
4class Solution:
5    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
6        anagram_map = defaultdict(list)
7
8        for string in strs:
9            count = [0] * 26
10
11            for char in string:
12                count[ord(char) - ord('a')] += 1
13
14            anagram_map[tuple(count)].append(string)
15        
16        return list(anagram_map.values())