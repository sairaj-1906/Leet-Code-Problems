1class Solution {
2    public String getHappyString(int n, int k) {
3        // Calculate the total maximum happy string of length n
4        // First char has 3 choices, remaining n-1 chars have 2 choices each
5        int totalStrings = 3 * (1 << (n - 1));
6
7        // If k is greater than the tool possible strings, return empty
8        if(k > totalStrings){
9            return "";
10
11        }
12
13        StringBuilder sb = new StringBuilder();
14        k--; // Convert k to 0-indexed for easier modular arithmetic
15        int blockSize = 1 << (n - 1); // Size of the block for each string character
16
17        // Determine the first character
18        int firstCharIdx = k / blockSize;
19        char prev = (char) ('a' + firstCharIdx);
20        sb.append(prev);
21        k %= blockSize;
22
23        // Determine the ramaining (n-1) characters
24        for(int i = 1; i < n; i++){
25            blockSize >>= 1;
26            int nextIdx = k / blockSize;
27
28            // Pick the next character based on the previous one to maintain lexiccographical order
29            if (prev == 'a'){
30                prev = (nextIdx == 0) ? 'b' : 'c';
31            } else if (prev == 'b'){
32                prev = (nextIdx == 0) ? 'a' : 'c';
33            } else {
34                prev = (nextIdx == 0) ? 'a' : 'b';
35            }
36
37            sb.append(prev);
38            k %= blockSize;
39        }
40
41        return sb.toString();
42    }
43}