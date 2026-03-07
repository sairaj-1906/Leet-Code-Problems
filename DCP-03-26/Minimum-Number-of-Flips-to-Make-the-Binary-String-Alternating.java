1class Solution {
2    public int minFlips(String s) {
3        int n = s.length();
4        int minFlips = Integer.MAX_VALUE;
5        
6        int diff1 = 0; // Mismatches for "010101..."
7        int diff2 = 0; // Mismatches for "101010..."
8        
9        // We simulate `s + s` by looping up to 2 * n
10        for (int i = 0; i < 2 * n; i++) {
11            // Use modulo to avoid actually concatenating the string (saves memory)
12            char c = s.charAt(i % n);
13            
14            // Expected characters for the two alternating patterns
15            char expected1 = (i % 2 == 0) ? '0' : '1';
16            char expected2 = (i % 2 == 0) ? '1' : '0';
17            
18            // Increment mismatches if current character doesn't match
19            if (c != expected1) diff1++;
20            if (c != expected2) diff2++;
21            
22            // Once our window exceeds size n, remove the effect of the leftmost character
23            if (i >= n) {
24                char leftChar = s.charAt((i - n) % n);
25                char leftExpected1 = ((i - n) % 2 == 0) ? '0' : '1';
26                char leftExpected2 = ((i - n) % 2 == 0) ? '1' : '0';
27                
28                if (leftChar != leftExpected1) diff1--;
29                if (leftChar != leftExpected2) diff2--;
30            }
31            
32            // When the window size reaches n, update the minimum flips required
33            if (i >= n - 1) {
34                minFlips = Math.min(minFlips, Math.min(diff1, diff2));
35            }
36        }
37        
38        return minFlips;
39    }
40}