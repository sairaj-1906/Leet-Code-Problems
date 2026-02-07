1class Solution {
2    public String longestPalindrome(String s) {
3        if (s == null || s.length() < 1) return "";
4        
5        int start = 0;
6        int end = 0;
7        
8        for (int i=0; i<s.length(); i++){
9            //Case 1: Odd length palindrome (center is character i)
10            int len1 = expandAroundCenter(s, i, i);
11            
12            //Case 2: Even length palindrome (center is between i and i+1)
13            int len2 = expandAroundCenter(s, i, i+1);
14            
15            //Get the maximum length found from eithe case
16            int len = Math.max(len1, len2);
17
18            // If we found a new longest palindrome, update the start and end indices
19            if (len > end - start){
20                // Calculate start/end based on the length and current center i
21                start = i - (len - 1) / 2;
22                end = i + len / 2;
23            }
24        }
25        // Return the substring (end is exclusive in Java substring method, so +1)
26        return s.substring(start, end + 1);
27    }
28    // Helper method to expand from the middle
29    private int expandAroundCenter(String s, int left, int right){
30        // While within bounds and characters match
31        while (left >= 0 && right<s.length() && s.charAt(left) == s.charAt(right)){
32            left--;
33            right++;
34        }
35        // Return the length of the palindrome found
36        // Note: loop terminates when left/right are invalid, so length is (right - left - 1)
37        return right - left - 1;
38    }
39}