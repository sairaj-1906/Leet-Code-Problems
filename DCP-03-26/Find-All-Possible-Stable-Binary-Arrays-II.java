1class Solution {
2    public int numberOfStableArrays(int zero, int one, int limit) {
3        int MOD = 1_000_000_007;
4        
5        // dp[i][j][0] -> arrays with i zeros, j ones, ending in 0
6        // dp[i][j][1] -> arrays with i zeros, j ones, ending in 1
7        long[][][] dp = new long[zero + 1][one + 1][2];
8
9        // Base cases initialization
10        // A sequence of just 0s up to the limit
11        for (int i = 1; i <= Math.min(zero, limit); i++) {
12            dp[i][0][0] = 1;
13        }
14        
15        // A sequence of just 1s up to the limit
16        for (int j = 1; j <= Math.min(one, limit); j++) {
17            dp[0][j][1] = 1;
18        }
19
20        // Fill the DP table
21        for (int i = 1; i <= zero; i++) {
22            for (int j = 1; j <= one; j++) {
23                
24                // Calculate ways to form an array ending in 0
25                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD;
26                if (i > limit) {
27                    dp[i][j][0] = (dp[i][j][0] - dp[i - 1 - limit][j][1] + MOD) % MOD;
28                }
29
30                // Calculate ways to form an array ending in 1
31                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD;
32                if (j > limit) {
33                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - 1 - limit][0] + MOD) % MOD;
34                }
35            }
36        }
37
38        // The answer is the sum of valid arrays ending in 0 and ending in 1
39        long totalStableArrays = (dp[zero][one][0] + dp[zero][one][1]) % MOD;
40        
41        return (int) totalStableArrays;
42    }
43}