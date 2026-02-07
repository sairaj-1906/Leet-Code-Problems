1import java.util.HashMap;
2class Solution 
3{
4    public int lengthOfLongestSubstring(String s) 
5    {
6        //Base Case
7        if (s == null || s.length() == 0)
8        {
9            return 0;
10        }
11        //Map to store the last seen index of each character
12        HashMap<Character, Integer>map = new HashMap<>();
13
14        int maxLength = 0;
15        int left = 0;
16        
17        for (int right = 0; right < s.length(); right++)
18        {
19            char currentChar = s.charAt(right);
20            //If we have seen this character before, and it is within the current window
21            if(map.containsKey(currentChar))
22            {
23                // Move the left pointer to the right of the previous occurrence.
24                // We use Math.max to prevent 'left' from moving backward if the 
25                // duplicate character was found before the current 'left'.
26                left = Math.max(left, map.get(currentChar)+1);
27            }
28            //Update the last seen index of the character
29            map.put(currentChar, right);
30            //Calculate the current window length and update max
31            maxLength = Math.max(maxLength, right - left + 1);
32        }
33        return maxLength;
34    }
35}