1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        n = len(nums)
7        k = k % n       # Handle cases where k > length of array
8
9        # Helper function to reverse a portion of array
10        def reverse(start: int, end: int) -> None:
11            while start < end:
12                nums[start], nums[end] = nums[end], nums[start]
13                start += 1
14                end -= 1
15        
16        #1. Reverse the entire array
17        reverse(0, n - 1)
18
19        #2. Reverse the first k elements
20        reverse(0, k - 1)
21
22        #3. Reverse the rest of the array
23        reverse(k, n - 1)