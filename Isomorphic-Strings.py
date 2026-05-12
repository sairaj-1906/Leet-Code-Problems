1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        map_s_to_t = {}
4        map_t_to_s = {}
5
6        for char_s, char_t in zip(s,t):
7            if char_s in map_s_to_t:
8                if map_s_to_t[char_s] != char_t:
9                    return False
10            else:
11                map_s_to_t[char_s] = char_t
12            
13            if char_t in map_t_to_s:
14                if map_t_to_s[char_t] != char_s:
15                    return False
16            else:
17                map_t_to_s[char_t] = char_s
18            
19        return True