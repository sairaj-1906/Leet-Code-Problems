1class Solution {
2    public boolean hasAlternatingBits(int n) {
3        // Step 1: XOR n with n shifted right by 1
4        int x = n ^ (n >> 1);
5        
6        // Step 2: Check if x is all 1s (i.e., of the form 111...1)
7        return (x & (x + 1)) == 0;
8    }
9}