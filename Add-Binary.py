1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        result = []
4        # Pointers for the end of each string
5        i, j = len(a) - 1, len(b) -1
6        carry = 0
7        # Loop while there are digits left in a, b, or a remaining carry
8        while i >= 0 or j >=0 or carry:
9            total = carry
10            # Add digit from a if available
11            if i >= 0:
12                total += int(a[i])
13                i -= 1
14            # Add digit from b if available
15            if j >= 0:
16                total += int(b[j])
17                j -= 1
18            # If total is 0 or 2, current bit is 0. If 1 or 3, current bit is 1.
19            result.append(str(total % 2))
20            # If total is 2 or 3, we have a carry (2 // 2 = 1)
21            carry = total // 2
22        # The result list is in reverse order (least significant bit first)
23        return "".join(reversed(result))
24        