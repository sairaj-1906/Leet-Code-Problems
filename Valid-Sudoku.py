1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        rows = [set() for _ in range(9)]
4        cols = [set() for _ in range(9)]
5        boxes = [set() for _ in range(9)]
6
7        for i in range(9):
8            for j in range(9):
9
10                num = board[i][j]
11
12                if num == ".":
13                    continue
14                
15                box = (i // 3) * 3 + (j // 3)
16
17                if num in rows[i] or num in cols[j] or num in boxes[box]:
18                    return False
19                
20                rows[i].add(num)
21                cols[j].add(num)
22                boxes[box].add(num)
23        
24        return True