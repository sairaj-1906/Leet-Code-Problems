1import java.util.ArrayList;
2import java.util.Collections;
3import java.util.List;
4
5class Solution {
6    public String makeLargestSpecial(String s) {
7        // Base case: if the string is empty, return it.
8        if (s == null || s.length() == 0) {
9            return s;
10        }
11        
12        int count = 0;
13        int i = 0;
14        List<String> substrings = new ArrayList<>();
15        
16        // Find top-level irreducible special substrings
17        for (int j = 0; j < s.length(); j++) {
18            if (s.charAt(j) == '1') {
19                count++;
20            } else {
21                count--;
22            }
23            
24            // When count reaches 0, we've found a complete special substring
25            if (count == 0) {
26                // Recursively process the inner string (removing the outer '1' and '0')
27                String inner = s.substring(i + 1, j);
28                String processedInner = makeLargestSpecial(inner);
29                
30                // Re-wrap with '1' and '0' and add to our list
31                substrings.add("1" + processedInner + "0");
32                
33                // Move the start pointer for the next top-level substring
34                i = j + 1;
35            }
36        }
37        
38        // Sort the top-level substrings in descending lexicographical order
39        Collections.sort(substrings, Collections.reverseOrder());
40        
41        // Join them back together
42        return String.join("", substrings);
43    }
44}