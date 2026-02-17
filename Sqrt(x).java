1class Solution {
2    public int mySqrt(int x) {
3        // Handle edge cases for 0 and 1
4        if (x < 2){
5            return x;
6        }
7        int left = 2;
8        int right = x/2;
9
10        while (left <= right){
11            // Calculate mid safely to avoid integer overflow
12            int mid = left + (right - left) / 2;
13
14            // Cast to long because mid*mid can exceed Integer.MAX_VALUE
15            long num = (long) mid*mid;
16
17            if (num == x){
18                return mid;
19            } else if (num < x){
20                left = mid + 1;
21            } else {
22                right = mid - 1;
23            }
24        }
25        // When the loop ends, 'right' will be the largest integer
26        // whose square is less than or equal to x.
27        return right;
28    }
29}