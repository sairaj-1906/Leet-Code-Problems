1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        max_profit = 0
4
5        # Iterate through the prices starting from the second day
6        for i in range(1, len(prices)):
7            # If there's a profit to be made from yesterday to today, capture it
8            if prices[i] > prices[i - 1]:
9                max_profit += prices[i] - prices[i - 1]
10            
11        return max_profit