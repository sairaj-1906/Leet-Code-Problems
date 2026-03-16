1import java.util.TreeSet;
2class Solution {
3    public int[] getBiggestThree(int[][] grid) {
4        int m = grid.length;
5        int n = grid[0].length;
6
7        // A TreeSet automatically keeps our sum sorted and ensures uniqueness
8        TreeSet<Integer> topSums = new TreeSet<>();
9
10        // Iterate over every cell in the grid to act as the top point of a rhombus
11        for(int i = 0; i < m; i++){
12            for(int j = 0; j < n; j++){
13                // L is the 'radius' or side length of the rhombus
14                // The conditions ensure the rhombus stays strictly within the grid bounds
15                for(int L = 0; i + 2 *L < m && j - L >= 0 && j + L < n; L++){
16                    int sum = 0;
17                    if(L == 0){
18                        // Area 0 rhombus (just the single cell)
19                        sum = grid[i][j];
20                    } else{
21                        // Traverse the 4 borders of the rhombus
22                        // Top to Right (excluding Right corner)
23                        for(int k = 0; k < L; k++) sum += grid[i + k][j + k];
24                        // Right to Bottom (excluding Bottom corner)
25                        for (int k = 0; k < L; k++) sum += grid[i + L + k][j + L - k];
26                        // Bottom to Left (excluding Left corner)
27                        for (int k = 0; k < L; k++) sum += grid[i + 2 * L - k][j - k];
28                        
29                        // Left to Top (excluding Top corner)
30                        for (int k = 0; k < L; k++) sum += grid[i + L - k][j - L + k];    
31                    }
32                    // Add to the TreeSet and maintain only the top 3 distinct sums
33                    topSums.add(sum);
34                    if(topSums.size() > 3){
35                        topSums.pollFirst(); // Removes the smallest element
36                    }
37                }
38            }
39        }
40        // Convert the TreeSet to an array in descending order
41        int[] result = new int[topSums.size()];
42        int index = result.length - 1;
43        for(int sum : topSums){
44            result[index--] = sum;
45        }
46        return result;
47    }
48}