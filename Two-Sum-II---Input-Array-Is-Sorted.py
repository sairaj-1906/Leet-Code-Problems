1from typing import List
2
3class Solution:
4    def twoSum(self, numbers: List[int], target: int) -> List[int]:
5        left, right = 0, len(numbers) - 1
6        while left < right:
7            s = numbers[left] + numbers[right]
8            if s == target:
9                return [left + 1, right + 1]
10            if s < target:
11                left += 1
12            else:
13                right -= 1
14        
15        return [-1, -1]