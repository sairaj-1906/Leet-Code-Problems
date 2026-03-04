1class Solution(object):
2    def findKthBit(self, n, k):
3        """
4        :type n: int
5        :type k: int
6        :rtype: str
7        """
8        # Base case
9        if n == 1:
10            return "0"
11        # Calculate the middle position for string S_n
12        # Length of S_n is 2^n-1, so the middle is at 2^(n-1)
13        mid = 1 << (n-1)
14
15        if k == mid:
16            # The middle bit is always "1" for n>1
17            return "1"
18        elif k < mid:
19            # If k is in the first half, it maps exactly to S_{n-1}
20            return self.findKthBit(n - 1, k)
21        else:
22            # If k is in the second half, it maps to an inberted, reserved S_{n-1}
23            # Find its symmetric position in the first half: (length + 1) - k = 2^n-k
24            corresponding_bit = self.findKthBit(n - 1, (1 << n) - k)
25
26            # Since the second half is inverted, we flip the result
27            return "0" if corresponding_bit == "1" else "1"