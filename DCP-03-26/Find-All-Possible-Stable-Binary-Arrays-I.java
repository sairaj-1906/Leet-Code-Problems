1class Solution {
2    public int numberOfStableArrays(int zero, int one, int limit) {
3        int MOD = 1000000007;
4        
5        // dp[i][j][0] represents stable arrays with i zeros, j ones, ending in 0
6        // dp[i][j][1] represents stable arrays with i zeros, j ones, ending in 1
7        long[][][] dp = new long[zero + 1][one + 1][2];
8        
9        // Base cases: Initialize valid sequences consisting entirely of zeros or ones up to the limit
10        for (int i = 1; i <= Math.min(zero, limit); i++) {
11            dp[i][0][0] = 1;
12        }
13        for (int j = 1; j <= Math.min(one, limit); j++) {
14            dp[0][j][1] = 1;
15        }
16        
17        // Fill the DP table
18        for (int i = 1; i <= zero; i++) {
19            for (int j = 1; j <= one; j++) {
20                
21                // Calculate arrays ending in 0
22                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD;
23                if (i - 1 - limit >= 0) {
24                    // Subtract combinations that exceed the limit
25                    dp[i][j][0] = (dp[i][j][0] - dp[i - 1 - limit][j][1] + MOD) % MOD;
26                }
27                
28                // Calculate arrays ending in 1
29                dp[i][j][1] = (dp[i][j - 1][1] + dp[i][j - 1][0]) % MOD;
30                if (j - 1 - limit >= 0) {
31                    // Subtract combinations that exceed the limit
32                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - 1 - limit][0] + MOD) % MOD;
33                }
34            }
35        }
36        
37        // The answer is the sum of valid configurations ending in either 0 or 1
38        long totalStableArrays = (dp[zero][one][0] + dp[zero][one][1]) % MOD;
39        return (int) totalStableArrays;
40    }
41}