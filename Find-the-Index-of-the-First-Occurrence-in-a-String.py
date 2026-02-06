1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        if not needle:
4            return 0
5        n = len(haystack)
6        m = len(needle)
7        #Iterate only up to the point where the needle can still fit
8        for i in range(n - m + 1):
9            #check if the substring matches the needle
10            if haystack[i : i + m] == needle:
11                return i
12        return -1
13        