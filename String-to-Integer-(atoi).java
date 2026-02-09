1class Solution {
2    public int myAtoi(String s) 
3    {
4        // 1. Initialize variables
5        int i = 0;
6        int n = s.length();
7        int sign = 1;
8        int result = 0;
9        // 2. Skip leading whitespace
10        while (i < n && s.charAt(i) == ' ')
11        {
12            i++;
13        }
14        // Check if string was just whitespace
15        if (i == n)
16        {
17            return 0;
18        }
19        // 3. Check for sign
20        if (s.charAt(i) == '-')
21        {
22            sign = -1;
23            i++;
24        }
25        else if (s.charAt(i) == '+')
26        {
27            sign = 1;
28            i++;
29        }
30        // 4. Convert digits
31        while (i < n)
32        {
33            char currentChar = s.charAt(i);
34            // If character is not a digit, stop
35            if (currentChar < '0' || currentChar > '9')
36            {
37                break;
38            }
39            int digit = currentChar - '0';
40            // 5. Check for overflow/underflow BEFORE updating result
41            // Check if result > 214748364
42            // OR if result == 214748364 AND digit > 7
43            if (result > Integer.MAX_VALUE / 10 || (result == Integer.MAX_VALUE / 10 && digit > Integer.MAX_VALUE % 10))
44            {
45                return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
46            }
47            result = result * 10 + digit;
48            i++;
49        }
50        return result * sign;
51    }
52}