1from typing import List
2
3class Solution:
4    def separateDigits(self, nums: List[int]) -> List[int]:
5        answer = []
6        for num in nums:
7            for digit in str(num):
8                answer.append(int(digit))
9        return answer