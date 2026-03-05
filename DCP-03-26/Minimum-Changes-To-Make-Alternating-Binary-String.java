1class Solution {
2    public int minOperations(String s) {
3        int countPatternA = 0;
4        int n = s.length();
5
6        for (int i = 0; i < n; i++){
7            // Check against Pattern A (starts with '0')
8            // In Pattern A, the expected numeric value at index i is (i % 2)
9            // Example: index 0 -> '0', index 1 -> '1', index 2 -> '0'
10            int expectedValue = i % 2;
11            int actualValue = s.charAt(i) - '0';
12
13            if (actualValue != expectedValue) {
14                countPatternA++;
15            }
16        }
17        // Return the minimum differences required to match either Pattern A or Pattern B
18        return Math.min(countPatternA, n - countPatternA);
19    }
20}