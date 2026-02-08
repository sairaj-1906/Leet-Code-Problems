1class Solution {
2    public String convert(String s, int numRows) {
3        // Edge case: If there is only 1 row, no zigzag pattern is formed.
4        if (numRows == 1 || numRows >= s.length()){
5            return s;
6        }
7        // Initialize a StringBuilder for each row
8        StringBuilder[] rows = new StringBuilder[numRows];
9        for (int i = 0; i < numRows; i++){
10            rows[i] = new StringBuilder();
11        }
12        int currentRow = 0;
13        boolean goingDown = false;
14        // Iterate through each character in the string
15        for (char c:s.toCharArray()){
16            rows[currentRow].append(c);
17            // If we are at the top or bottom row, reverse direction
18            if (currentRow == 0 || currentRow == numRows -1){
19                goingDown = !goingDown;
20            }
21            // Update the current row based on direction
22            currentRow += goingDown ? 1 : -1;
23        }
24        // Combine all rows into a single string
25        StringBuilder result = new StringBuilder();
26        for (StringBuilder row : rows){
27            result.append(row);
28        }
29        return result.toString();
30    }
31}