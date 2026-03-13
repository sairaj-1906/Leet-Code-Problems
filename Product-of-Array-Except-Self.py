1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        answer = [1] * n
5
6        # prefix product
7        prefix = 1
8        for i in range(n):
9            answer[i] = prefix
10            prefix *= nums[i]
11        
12        # suffix product
13        suffix = 1
14        for i in range(n-1, -1, -1):
15            answer[i] *= suffix
16            suffix *= nums[i]
17        
18        return answer