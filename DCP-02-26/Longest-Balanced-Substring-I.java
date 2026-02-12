1import java.util.*;
2class Solution {
3    public int longestBalanced(String s) {
4        int n = s.length();
5        int maxLen = 0;
6
7        // Iterate over all possible starting points of the substring
8        for (int i = 0; i < n; i++) {
9            
10            // Optimization: If the remaining length is less than maxLen already found,
11            // we can't find a better result, so we stop.
12            if (n - i <= maxLen) break;
13
14            // Frequency array for the current substring window
15            int[] freq = new int[26];
16            
17            // Iterate over all ending points for the current start 'i'
18            for (int j = i; j < n; j++) {
19                
20                // Add current character to frequency
21                freq[s.charAt(j) - 'a']++;
22
23                // Check if the current window is balanced
24                if (isBalanced(freq)) {
25                    maxLen = Math.max(maxLen, j - i + 1);
26                }
27            }
28        }
29        
30        return maxLen;
31    }
32
33    // Helper method to check if the frequency array is balanced
34    private static boolean isBalanced(int[] freq) {
35        int commonCount = 0;
36        
37        for (int count : freq) {
38            // Ignore characters that are not present
39            if (count == 0) continue;
40            
41            // If this is the first non-zero count we see, store it as the reference
42            if (commonCount == 0) {
43                commonCount = count;
44            } 
45            // If we encounter a count different from the reference, it's not balanced
46            else if (count != commonCount) {
47                return false;
48            }
49        }
50        return true;
51    }
52}