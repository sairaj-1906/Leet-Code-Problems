1import math
2class Solution:
3    def maxSumTrionic(self, nums: List[int]) -> int:
4        """
5        Calculates the maximum sum of a trionic subarray.
6        A trionic subarray nums[l...r] is defined by l < p < q < r such that:
7        - nums[l...p] is strictly increasing
8        - nums[p...q] is strictly decreasing
9        - nums[q...r] is strictly increasing
10        """
11        n = len(nums)
12        if n < 4:
13            return 0  # Impossible to form l < p < q < r with fewer than 4 elements
14        # Initialize states to negative infinity
15        # inc1: max sum of strictly increasing subarray ending at current index
16        # dec:  max sum of (Inc -> Dec) ending at current index
17        # inc2: max sum of (Inc -> Dec -> Inc) ending at current index
18        prev_inc1 = -math.inf
19        prev_dec = -math.inf
20        prev_inc2 = -math.inf
21        
22        global_max = -math.inf
23        
24        for i in range(1, n):
25            curr = nums[i]
26            prev = nums[i-1]
27            # Current states initialized to -inf
28            curr_inc1 = -math.inf
29            curr_dec = -math.inf
30            curr_inc2 = -math.inf
31            
32            if curr > prev:
33                # 1. Update inc1 (First Increasing)
34                # Either extend existing inc1 or start new increasing seq of length 2
35                curr_inc1 = max(prev_inc1 + curr, prev + curr)
36                # 2. Update inc2 (Second Increasing - Final Phase)
37                # Transition from dec state to inc2, or extend existing inc2
38                if prev_dec != -math.inf:
39                    # We can only transition if a valid decreasing sequence existed
40                    curr_inc2 = max(prev_dec + curr, prev_inc2 + curr)
41                elif prev_inc2 != -math.inf:
42                    # If we were already in inc2, we can extend it
43                    curr_inc2 = prev_inc2 + curr
44            
45            elif curr < prev:
46                # Update dec (Decreasing - Middle Phase)
47                # Transition from inc1 to dec, or extend existing dec
48                if prev_inc1 != -math.inf:
49                    # We can pivot from increasing to decreasing
50                    curr_dec = max(prev_inc1 + curr, prev_dec + curr)
51                elif prev_dec != -math.inf:
52                    # If we were already in dec, extend it
53                    curr_dec = prev_dec + curr
54            
55            # Update global max with any valid completed trionic subarray (inc2)
56            if curr_inc2 != -math.inf:
57                global_max = max(global_max, curr_inc2)
58            # Move current states to previous for next iteration
59            prev_inc1 = curr_inc1
60            prev_dec = curr_dec
61            prev_inc2 = curr_inc2
62        
63        return global_max if global_max != -math.inf else 0       