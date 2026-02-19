1class Solution {
2    public int countBinarySubstrings(String s) {
3        int prev = 0;   // Length of the previous consecutive group
4        int curr = 1;   // Length of the current consecutive group
5        int count = 0;  // Total valid substrings found
6
7        for (int i=1; i<s.length(); i++) {
8            // If the character is the same as the previous one, extend the current group
9            if (s.charAt(i) == s.charAt(i-1)){
10                curr++;
11            }
12            // If the character changes, the current group becomes the previous group
13            else{
14                prev = curr;
15                curr = 1;
16            }
17            // If the previous group is large enough to pair with the current group's characters
18            if (prev>=curr){
19                count++;
20            }
21        }
22        return count;
23    }
24}