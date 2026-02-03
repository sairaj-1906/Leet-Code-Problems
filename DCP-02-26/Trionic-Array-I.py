1class Solution(object):
2    def isTrionic(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        n = len(nums)
8        if n<3:
9            return False
10        i=0
11        #First strictly increasing segment (to peak p)
12        while i+1 < n and nums[i] < nums[i+1]:
13            i += 1
14        #Valid check: we must have increased at least once, and not reached the end
15        if i == 0 or i == n-1:
16            return False
17        #Strictly decreasing segment (to valley q)
18        p = i
19        while i+1 < n and nums[i] > nums[i+1]:
20            i += 1
21        #Valid check: we must have decreased at least once from p
22        if i == p or i == n-1:
23            return False
24        #Strict increasing segment
25        q = i
26        while i + 1 < n and nums[i] < nums[i+1]:
27            i += 1
28        #valid check: must have increased from q and reach the final index
29        return i == n-1 and i > q
30