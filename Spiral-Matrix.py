1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        result = []
4
5        top = 0
6        bottom = len(matrix) - 1
7        left = 0
8        right = len(matrix[0]) - 1
9
10        while top <= bottom and left <= right:
11            for i in range(left, right + 1):
12                result.append(matrix[top][i])
13            top += 1
14
15            for i in range(top, bottom + 1):
16                result.append(matrix[i][right])
17            right -= 1
18
19            if top <= bottom:
20                for i in range(right, left - 1, -1):
21                    result.append(matrix[bottom][i])
22                bottom -= 1
23            
24            if left <= right:
25                for i in range(bottom, top -1, -1):
26                    result.append(matrix[i][left])
27                left += 1
28        
29        return result