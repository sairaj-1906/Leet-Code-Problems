1class Solution:
2    def rotateGrid(self, grid, k):
3        m, n = len(grid), len(grid[0])
4
5        layers = min(m, n) // 2
6
7        for layer in range(layers):
8
9            elements = []
10
11            top, left = layer, layer
12            bottom, right = m - layer - 1, n - layer - 1
13
14            for j in range(left, right + 1):
15                elements.append(grid[top][j])
16
17            for i in range(top + 1, bottom):
18                elements.append(grid[i][right])
19
20            for j in range(right, left - 1, -1):
21                elements.append(grid[bottom][j])
22
23            for i in range(bottom - 1, top, -1):
24                elements.append(grid[i][left])
25
26            length = len(elements)
27            rotate = k % length
28            rotated = elements[rotate:] + elements[:rotate]
29
30            idx = 0
31
32            for j in range(left, right + 1):
33                grid[top][j] = rotated[idx]
34                idx += 1
35
36            for i in range(top + 1, bottom):
37                grid[i][right] = rotated[idx]
38                idx += 1
39
40            for j in range(right, left - 1, -1):
41                grid[bottom][j] = rotated[idx]
42                idx += 1
43
44            for i in range(bottom - 1, top, -1):
45                grid[i][left] = rotated[idx]
46                idx += 1
47
48        return grid