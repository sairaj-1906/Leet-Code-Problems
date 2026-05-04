1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        n = len(matrix)
7
8        for i in range(n):
9            for j in range(i + 1, n):
10                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
11        
12        for i in range(n):
13            matrix[i].reverse()