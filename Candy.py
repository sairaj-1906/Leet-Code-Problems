1from typing import List
2class Solution:
3    def candy(self, ratings: List[int]) -> int:
4        n = len(ratings)
5        # Every child must have atleast one candy
6        candies = [1] * n
7
8        # Left to Right Pass
9        # Check if a cgild has a higher rating than their left neighbor
10        for i in range(1, n):
11            if ratings[i] > ratings[i - 1]:
12                candies[i] = candies[i - 1] + 1
13        
14        # Right-to-Left Pass
15        # Check if a child has a higher rating than their right neighbor
16        for i in range(n - 2, -1, -1):
17            if ratings[i] > ratings[i + 1]:
18                # We use max() to ensure we don't break the condition 
19                # satisfied in the left-to-right pass
20                candies[i] = max(candies[i], candies[i + 1] + 1)
21        
22        # Return the total minimum candies needed
23        return sum(candies)