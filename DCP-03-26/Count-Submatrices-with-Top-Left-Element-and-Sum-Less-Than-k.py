1class Solution:
2    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
3        m = len(grid)
4        n = len(grid[0])
5
6        # Built prefix sum in place
7        for i in range(m):
8            for j in range(n):
9                top = grid[i-1][j] if i > 0 else 0
10                left = grid[i][j-1] if j > 0 else 0
11                diag = grid[i-1][j-1] if i > 0 and j > 0 else 0
12
13                grid[i][j] += top + left - diag
14        
15        # count valid submatrices
16        count = 0
17        for i in range(m):
18            for j in range(n):
19                if grid[i][j] <= k:
20                    count += 1
21        
22        return count