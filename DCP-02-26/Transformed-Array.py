1class Solution:
2    def constructTransformedArray(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        result = [0]*n
5
6        for i in range(n):
7            #Calculate steps.
8            #Python's % operator handles negative wrapping aitomatically.
9            target_index = (i + nums[i]) % n
10            #Assign the value found at the tarhet index to result [i]
11            result[i] = nums[target_index]
12        return result