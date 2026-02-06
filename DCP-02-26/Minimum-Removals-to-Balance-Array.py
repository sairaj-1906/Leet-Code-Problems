1class Solution:
2    def minRemoval(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        n = len(nums)
5        max_len = 0
6        left = 0
7        # Use a sliding window to find the longest balanced subarray
8        for right in range(n):
9            # Shrink the window from the left if it violates the condition
10            while nums[right] > nums[left] * k:
11                left += 1
12            # Current window [left...right] is balanced
13            max_len = max(max_len, right - left + 1)
14        return n - max_len
15        