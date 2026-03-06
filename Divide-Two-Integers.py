1class Solution:
2    def divide(self, dividend: int, divisor: int) -> int:
3        # Constants for 32-bit integer limits
4        INT_MAX = 2147483647  # 2**31 - 1
5        INT_MIN = -2147483648 # -2**31
6        
7        # Handle the single overflow edge case
8        if dividend == INT_MIN and divisor == -1:
9            return INT_MAX
10            
11        # Determine the sign of the final quotient
12        # If one is negative and the other is positive, the result is negative
13        is_negative = (dividend < 0) != (divisor < 0)
14        
15        # Convert both to positive numbers for easier calculation
16        abs_dividend = abs(dividend)
17        abs_divisor = abs(divisor)
18        
19        quotient = 0
20        
21        # Start from the largest possible shift (31 bits for a 32-bit integer)
22        for i in range(31, -1, -1):
23            # If divisor * (2^i) fits into the remaining dividend
24            if (abs_divisor << i) <= abs_dividend:
25                # Subtract divisor * (2^i) from the dividend
26                abs_dividend -= (abs_divisor << i)
27                # Add 2^i to our quotient
28                quotient += (1 << i)
29                
30        # Apply the original sign
31        if is_negative:
32            quotient = -quotient
33            
34        return quotient