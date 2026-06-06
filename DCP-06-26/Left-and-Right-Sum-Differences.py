1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        total_sum = sum(nums)
4        left_sum = 0
5        right_sum = total_sum
6        answer = []
7
8        for num in nums:
9            right_sum -= num
10            answer.append(abs(left_sum - right_sum))
11            left_sum += num
12
13        return answer