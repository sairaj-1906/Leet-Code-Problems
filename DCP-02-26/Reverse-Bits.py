1class Solution:
2    def reverseBits(self, n: int) -> int:
3        result = 0
4        for _ in range(32):
5            # 1. Shift result to the left to open up the LSB
6            result = result << 1
7
8            # 2. Add the LSB of n to result
9            bit = n & 1
10            result = result | bit
11
12            # 3. Shift n to the right to process the next bit
13            n = n >> 1
14        
15        return result
16        