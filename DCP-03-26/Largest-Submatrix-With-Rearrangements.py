1class Solution:
2    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
3        m = len(matrix)
4        n = len(matrix[0])
5        max_area = 0
6
7        # Calculate consecutive height for each column
8        for i in range(m):
9            for j in range(n):
10                # If it's a 1 and not the first row, add the height from the row above
11                if matrix[i][j] != 0 and i > 0:
12                    matrix[i][j] += matrix[i-1][j]
13            
14            # Sort the current row's height in decending order
15            sorted_height = sorted(matrix[i], reverse=True)
16
17            # Calculate the maximum possible are using the sorted heights
18            for k in range(n):
19                # area = height * width
20                area = sorted_height[k] * (k + 1)
21                max_area = max(max_area, area)
22
23        return max_area