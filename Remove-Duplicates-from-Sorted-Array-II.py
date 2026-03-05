1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        # If the array has 2 or fewer elements, they are all valid
4        if len(nums) <=2:
5            return len(nums)
6
7        # k keeps track of the index for the next valid element
8        k = 2
9
10        # Iterate starting from the 3rd element
11        for i in range(2, len(nums)):
12            # If the current element is different from the element 2 steps back
13            # in our valid section, it's safe to include it.
14            if nums[i] != nums[k - 2]:
15                nums[k] = nums[i]
16                k += 1
17        
18        return k