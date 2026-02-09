1class Solution:
2    def intToRoman(self, num: int) -> str:
3        # Define the mapping of values to symbols in descending order.
4        # This includes standard symbols and the subtractive instances (IV, IX, etc.)
5        value_map = [
6            (1000, "M"),
7            (900, "CM"),
8            (500, "D"),
9            (400, "CD"),
10            (100, "C"),
11            (90, "XC"),
12            (50, "L"),
13            (40, "XL"),
14            (10, "X"),
15            (9, "IX"),
16            (5, "V"),
17            (4, "IV"),
18            (1, "I")
19        ]
20        result = []
21        # Iterate through each symbol starting from the largest
22        for value, symbol in value_map:
23            # If the input number is 0, we are done
24            if num == 0:
25                break
26            # Determine how many times the current value fits into num
27            count, num = divmod(num, value)
28            # Append the symbol 'count' times
29            result.append(symbol * count)
30        return "".join(result)