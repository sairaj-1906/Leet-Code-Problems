1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        mapping = {')':'(', '}':'{', ']':'['}
5        for ch in s:
6            if ch in mapping:
7                if not stack or stack[-1] != mapping[ch]:
8                    return False
9                stack.pop()
10            else:
11                stack.append(ch)
12        return not stack