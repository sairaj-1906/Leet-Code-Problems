1class Solution:
2    def countPrimeSetBits(self, left: int, right: int) -> int:
3        # Precompute prime numbers up to the maximum possible set bits
4        # Since right <= 10^6, max set bits = 20 (because 2^20 > 10^6)
5
6        primes = {2, 3, 5, 7, 11, 13, 17, 19}
7
8        def count_set_bits(n: int) -> int:
9            # Count number of 1s in binary representation
10
11            return bin(n).count('1')
12
13        count = 0
14
15        for num in range (left, right + 1):
16            if count_set_bits(num) in primes:
17                count += 1
18        return count