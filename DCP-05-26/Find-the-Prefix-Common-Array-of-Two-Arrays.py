1from typing import List
2
3class Solution:
4    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
5        n = len(A)
6        freq = [0] * (n + 1)
7        C = []
8        common_count = 0
9
10        for i in range(n):
11            freq[A[i]] += 1
12            if freq[A[i]] == 2:
13                common_count += 1
14
15            freq[B[i]] += 1
16            if freq[B[i]] == 2:
17                common_count += 1
18
19            C.append(common_count)
20
21        return C
22