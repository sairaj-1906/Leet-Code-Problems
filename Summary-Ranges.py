1from typing import List
2
3
4class Solution:
5    def summaryRanges(self, nums: List[int]) -> List[str]:
6        ranges = []
7        i = 0
8
9        while i < len(nums):
10            start = nums[i]
11
12            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
13                i += 1
14
15            end = nums[i]
16
17            if start == end:
18                ranges.append(str(start))
19            else:
20                ranges.append(f"{start}->{end}")
21
22            i += 1
23
24        return ranges
25