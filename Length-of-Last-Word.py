1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        length = 0
4        i = len(s) - 1
5        # Step 1: Skip any trailing spaces at the end of the string
6        while i >= 0 and s[i] == ' ':
7            i -= 1
8        # Step 2: Count characters of the last word until we hit a space or start of string
9        while i >= 0 and s[i] != ' ':
10            length += 1
11            i -= 1
12        return length