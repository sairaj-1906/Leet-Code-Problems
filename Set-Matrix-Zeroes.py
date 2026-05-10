1class Solution:
2    def setZeroes(self, matrix):
3        rows = len(matrix)
4        cols = len(matrix[0])
5
6        first_row = False
7        first_col = False
8
9        # Check first row
10        for j in range(cols):
11            if matrix[0][j] == 0:
12                first_row = True
13
14        # Check first column
15        for i in range(rows):
16            if matrix[i][0] == 0:
17                first_col = True
18
19        # Use first row and column as markers
20        for i in range(1, rows):
21            for j in range(1, cols):
22                if matrix[i][j] == 0:
23                    matrix[i][0] = 0
24                    matrix[0][j] = 0
25
26        # Set cells to zero using markers
27        for i in range(1, rows):
28            for j in range(1, cols):
29                if matrix[i][0] == 0 or matrix[0][j] == 0:
30                    matrix[i][j] = 0
31
32        # Set first row to zero
33        if first_row:
34            for j in range(cols):
35                matrix[0][j] = 0
36
37        # Set first column to zero
38        if first_col:
39            for i in range(rows):
40                matrix[i][0] = 0