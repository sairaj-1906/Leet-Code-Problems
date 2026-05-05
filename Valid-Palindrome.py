1import re
2
3class Solution:
4    def isPalindrome(self, s: str) -> bool:
5        s = s.lower()
6
7        s = re.sub(r'[^a-z0-9]', '', s)
8
9        return s == s[::-1]