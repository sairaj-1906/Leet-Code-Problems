1from typing import List
2
3class Solution:
4    def gameOfLife(self, board: List[List[int]]) -> None:
5        """
6        Do not return anything, modify board in-place instead.
7        """
8        m, n = len(board), len(board[0])
9
10        def count_live_neighbors(r, c):
11            count = 0
12            for i in range(r-1, r+2):
13                for j in range(c-1, c+2):
14                    if (i == r and j == c) or i < 0 or j < 0 or i >= m or j >= n:
15                        continue
16                    if abs(board[i][j]) == 1:
17                        count += 1
18            return count
19
20        for i in range(m):
21            for j in range(n):
22                live_neighbors = count_live_neighbors(i, j)
23                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
24                    board[i][j] = -1
25                if board[i][j] == 0 and live_neighbors == 3:
26                    board[i][j] = 2
27
28        for i in range(m):
29            for j in range(n):
30                if board[i][j] > 0:
31                    board[i][j] = 1
32                else:
33                    board[i][j] = 0