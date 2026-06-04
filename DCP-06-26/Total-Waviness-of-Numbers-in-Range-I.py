1class Solution:
2    def totalWaviness(self, num1: int, num2: int) -> int:
3        total_waviness = 0
4
5        for num in range(num1, num2 + 1):
6            num_str = str(num)
7            n = len(num_str)
8
9            if n < 3:
10                continue
11
12            for i in range(1, n - 1):
13                prev_digit = num_str[i - 1]
14                curr_digit = num_str[i]
15                next_digit = num_str[i + 1]
16
17                if curr_digit > prev_digit and curr_digit > next_digit:
18                    total_waviness += 1
19
20                elif curr_digit < prev_digit and curr_digit < next_digit:
21                    total_waviness += 1
22
23        return total_waviness
24