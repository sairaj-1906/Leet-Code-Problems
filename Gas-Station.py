1from typing import List
2class Solution:
3    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
4        # If total gas is less than total cost, we can't complete the journey
5        if sum(gas) < sum(cost):
6            return -1
7        
8        current_tank = 0
9        start_index = 0
10
11        for i in range(len(gas)):
12            current_tank += gas[i] - cost[i]
13            
14            # If our tank goes -ve, the route from start_index to i is invalid
15            # The next potential starting point is i + 1
16            if current_tank < 0:
17                start_index = i + 1
18                current_tank = 0
19        
20        return start_index