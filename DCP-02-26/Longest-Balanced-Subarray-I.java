1import java.util.HashSet;
2import java.util.Set;
3class Solution {
4    public int longestBalanced(int[] nums) {
5        int n = nums.length;
6        int maxLen = 0;
7
8        // Iterate over every possible starting point of the subarray
9        for (int i = 0; i < n; i++) {
10            // Use HashSets to track distinct numbers for the current subarray
11            Set<Integer> distinctEvens = new HashSet<>();
12            Set<Integer> distinctOdds = new HashSet<>();
13
14            // Extend the subarray from start point 'i' to 'j'
15            for (int j = i; j < n; j++) {
16                // Add current number to the respective set
17                if (nums[j] % 2 == 0) {
18                    distinctEvens.add(nums[j]);
19                } else {
20                    distinctOdds.add(nums[j]);
21                }
22
23                // Check if the number of distinct evens equals distinct odds
24                if (distinctEvens.size() == distinctOdds.size()) {
25                    // Update maxLen. The length is index difference + 1
26                    maxLen = Math.max(maxLen, j - i + 1);
27                }
28            }
29        }
30
31        return maxLen;
32    }
33}