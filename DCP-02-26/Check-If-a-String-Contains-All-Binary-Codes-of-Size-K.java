1import java.util.HashSet;
2import java.util.Set;
3
4class Solution {
5    public boolean hasAllCodes(String s, int k) {
6        // Edge case: if the string is too short to possibly contain all combinations
7        if (s.length() < (1 << k) + k - 1) {
8            return false;
9        }
10
11        Set<String> seen = new HashSet<>();
12        int targetCount = 1 << k; // This is equivalent to 2^k
13        
14        // Slide a window of size k across the string
15        for (int i = 0; i <= s.length() - k; i++) {
16            String currentSubstring = s.substring(i, i + k);
17            
18            // If it's a new substring, add it to our set
19            if (seen.add(currentSubstring)) {
20                targetCount--;
21                
22                // If we found all 2^k combinations, we can stop early
23                if (targetCount == 0) {
24                    return true;
25                }
26            }
27        }
28        
29        return false;
30    }
31}