1class Solution {
2    public int bitwiseComplement(int n) {
3        // Edge case: The binary representation of 0 is just "0",
4        // so its complement is "1"
5        if(n == 0){
6            return 1;
7        }
8
9        int temp = n;
10        int mask = 0;
11
12        // Built a mask of 1s that is exactly the same length as n's bunary representation 
13        while(temp > 0){
14            // Shift mask to the left by 1 and add a 1 at the end
15            mask = (mask << 1) | 1;
16
17            // Shift temp to the right to count down the bits
18            temp >>= 1;
19        }
20
21        // XOR n with the all-1s mask to flip every bit
22        return n ^ mask;
23    }
24}