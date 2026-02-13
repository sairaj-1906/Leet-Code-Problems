1import java.util.Arrays;
2class Solution {
3    public int[] plusOne(int[] digits) {
4        int n = digits.length;
5
6        // Iterate backwards from the last digit to the first
7        for (int i = n - 1; i >= 0; i--){
8            // Case 1: The digit is less than 9
9            // Simply increment it and return the array immediately.
10            // Example: [1, 2, 3] -> 3 becomes 4 -> return [1, 2, 4]
11            if (digits[i] < 9){
12                digits[i]++;
13                return digits;
14            }
15            // Case 2: The digit is 9
16            // It becomes 0, and we carry over to the next iteration (next digit to the left).
17            // Example: [1, 2, 9] -> 9 becomes 0 -> loop continues to handle the 2
18            digits[i] = 0;
19        }
20        // Case 3: All digits were 9 (Overflow)
21        // If the loop finishes, it means we had something like [9, 9, 9].
22        // All digits have become 0. We need to resize the array.
23        // Create a new array with length n + 1.
24        // Example: [9, 9] -> loop makes it [0, 0] -> we need [1, 0, 0]
25        int[] newNumber = new int[n+1];
26        newNumber[0] = 1;           // The rest are initialized to 0 by default in Java
27
28        return newNumber;
29    }
30}