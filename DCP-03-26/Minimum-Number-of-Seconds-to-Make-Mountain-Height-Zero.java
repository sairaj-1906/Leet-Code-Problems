1class Solution {
2    
3    public long maxHeight(long time, int t) {
4        // Solve t * x(x+1)/2 <= time
5        long left = 0, right = (long)1e6;
6        
7        while (left <= right) {
8            long mid = left + (right - left) / 2;
9            long required = (long)t * mid * (mid + 1) / 2;
10            
11            if (required <= time) {
12                left = mid + 1;
13            } else {
14                right = mid - 1;
15            }
16        }
17        
18        return right;
19    }
20    
21    public long minNumberOfSeconds(int mountainHeight, int[] workerTimes) {
22        
23        long left = 0, right = (long)1e18;
24        long ans = right;
25        
26        while (left <= right) {
27            long mid = left + (right - left) / 2;
28            
29            long total = 0;
30            
31            for (int t : workerTimes) {
32                total += maxHeight(mid, t);
33                if (total >= mountainHeight) break;
34            }
35            
36            if (total >= mountainHeight) {
37                ans = mid;
38                right = mid - 1;
39            } else {
40                left = mid + 1;
41            }
42        }
43        
44        return ans;
45    }
46}