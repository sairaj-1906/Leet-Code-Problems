1from typing import List
2
3class Solution:
4    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
5        m, n = len(boxGrid), len(boxGrid[0])
6        grid = [row[:] for row in boxGrid]
7
8        for i in range(m):
9            empty = n - 1
10            j = n - 1
11            while j>=0:
12                if grid[i][j] == '*':
13                    empty = j - 1
14                elif grid[i][j] == '#':
15                    if j != empty:
16                        grid[i][empty] = '#'
17                        grid[i][j] = '.'
18                    empty -= 1
19                j -= 1
20        
21        rotated = [[''] * m for _ in range(n)]
22        for i in range(m):
23            for j in range(n):
24                rotated[j][m - 1 - i] = grid[i][j]
25        
26        return rotated