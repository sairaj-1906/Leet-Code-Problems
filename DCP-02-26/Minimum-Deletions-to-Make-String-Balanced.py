1class Solution:
2    def minimumDeletions(self, s: str) -> int:
3        count_b = 0
4        min_deletion = 0
5
6        for char in s:
7            if char == 'b':
8                count_b += 1
9            else: # char is 'a'
10                # If we find an 'a' and we have seen 'b's before,
11                # we have a violation. We delete one character to fix it.
12                if count_b >0:
13                    min_deletion += 1
14                    count_b -= 1
15        
16        return min_deletion