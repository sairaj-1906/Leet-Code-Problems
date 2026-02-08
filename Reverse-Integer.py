1class Solution:
2    def reverse(self, x: int) -> int:
3        # Define 32-bit signed integer limits
4        INT_MIN, INT_MAX = -2**31, 2**31 - 1
5        res = 0
6        # Handle negative numbers by working with absolute value
7        # and reapplying sign later
8        sign = -1 if x < 0 else 1
9        x = abs(x)
10
11        while x != 0:
12            # Pop the last digit
13            digit = x % 10
14            x //= 10
15
16            # Check if appending the digit causes overflow
17            # In a strict 32-bit environment, you would check BEFORE
18            # the multiplication (res * 10). 
19            # Since Python handles large ints safely, we can check 
20            # just before returning or during the loop.
21            if res > (INT_MAX - digit) // 10:
22                return 0
23            
24            # Push the digit
25            res = res * 10 + digit
26        
27        return sign * res