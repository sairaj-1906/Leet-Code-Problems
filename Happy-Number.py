1class Solution:
2    def isHappy(self, n: int) -> bool:
3        def get_next(number):
4            total_sum = 0
5            while number > 0:
6                number, digit = divmod(number, 10)
7                total_sum += digit ** 2
8            return total_sum
9        
10        seen = set()
11        while n != 1 and n not in seen:
12            seen.add(n)
13            n = get_next(n)
14
15        return n == 1