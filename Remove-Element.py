1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        #k acts as the boundary for elements not equal to vel
4        k = 0
5        for i in range(len(nums)):
6            if nums[i] != val:
7                #Move the 'good' element to thr front
8                nums[k] = nums[i]
9                k += 1
10        return k
11        