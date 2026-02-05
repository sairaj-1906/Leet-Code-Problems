1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if not nums:
4            return 0
5        
6        # 'i' tracks the position of the last unique element found
7        i = 0
8        
9        # 'j' scans the array starting from the second element
10        for j in range(1, len(nums)):
11            # If the current element (j) is different from the last unique one (i)
12            if nums[j] != nums[i]:
13                # 1. Advance the unique pointer
14                i += 1
15                # 2. Overwrite the next position with the new unique value
16                nums[i] = nums[j]
17        
18        # Return the count (index + 1)
19        return i + 1