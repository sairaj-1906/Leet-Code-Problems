1class Solution:
2    def findDifferentBinaryString(self, nums: List[str]) -> str:
3        # Denerate the unique string by flipping the diagonal bits
4        ans = []
5        for i in range(len(nums)):
6            current_bit = nums[i][i]
7            # Flip '0' to '1' and '1' to '0'
8            ans.append('1' if current_bit == '0' else '0')
9        
10        return "".join(ans)