1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price = float('inf')
4        max_profit = 0
5
6        for price in prices:
7            # Update the lowest price we've seen so far
8            if price < min_price:
9                min_price = price
10            # If selling today yeilds a better profit, update max_profit
11            elif price - min_price > max_profit:
12                max_profit = price - min_price
13        
14        return max_profit
15        