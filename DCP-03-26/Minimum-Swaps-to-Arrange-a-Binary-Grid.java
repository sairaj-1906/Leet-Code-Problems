1class Solution {
2    public int minSwaps(int[][] grid) {
3        int n = grid.length;
4        int[] trailingZeros = new int[n];
5
6        // Step 1: Count the number of trailing zeros for each row
7        for (int i = 0; i < n; i++) {
8            int count = 0;
9            for (int j = n-1; j >= 0; j--) {
10                if (grid[i][j] == 0) {
11                    count++;
12                } else {
13                    break;
14                }
15            }
16            trailingZeros[i] = count;
17        }
18        int swaps = 0;
19        // Step 2: Use a greedy approach to place the correct row at each index
20        for (int i = 0; i < n; i++) {
21            int targetZeros = n - 1 - i;
22            int j = i;
23
24            // Find the closest row (starting from i) that has enough trailing zeros
25            while (j < n && trailingZeros[j] < targetZeros) {
26                j++;
27            }
28            // If no such row is found, it's impossible to make the grid valid
29            if (j == n){
30                return -1;
31            }
32            // The number of swaps is the distance from its current position to 'i'
33            swaps += (j - i);
34
35            // Step 3: Shift the elements down to simulate pulling the row up
36            int currentVal = trailingZeros[j];
37            while (j > i) {
38                trailingZeros[j] = trailingZeros[j - 1];
39                j--;
40            }
41            // Place the matched row's zero count at the current index
42            trailingZeros[i] = currentVal;
43        }
44        return swaps;
45    }
46}