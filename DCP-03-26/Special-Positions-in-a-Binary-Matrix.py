1class Solution(object):
2    def numSpecial(self, mat):
3        """
4        :type mat: List[List[int]]
5        :rtype: int
6        """
7        m, n = len(mat), len(mat[0])
8
9        # Precomputr the sum of the 1s in each row and each column
10        row_sums = [sum(row) for row in mat]
11        col_sums = [sum(mat[i][j] for i in range(m)) for j in range (n)]
12        
13        special_count = 0
14
15        # Check each position to see if it meets the "special" criteria
16        for i in range(m):
17            for j in range(n):
18                # It's special if the cell is 1, and it's the ONLY 1 in it's row and column
19                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
20                    special_count += 1
21        
22        return special_count