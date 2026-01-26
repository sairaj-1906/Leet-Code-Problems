1#include <vector>
2#include <algorithm>
3#include <climits> // For INT_MAX
4
5class Solution {
6public:
7    std::vector<std::vector<int>> minimumAbsDifference(std::vector<int>& arr) {
8        // 1. Sort the array
9        std::sort(arr.begin(), arr.end());
10        
11        std::vector<std::vector<int>> result;
12        int min_diff = INT_MAX;
13        
14        // 2. Iterate to find min_diff and collect pairs
15        for (int i = 0; i < arr.size() - 1; ++i) {
16            int curr_diff = arr[i+1] - arr[i];
17            
18            // If we find a new smaller difference, clear previous results
19            if (curr_diff < min_diff) {
20                min_diff = curr_diff;
21                result.clear(); // Discard pairs with larger differences
22                result.push_back({arr[i], arr[i+1]});
23            }
24            // If the difference matches the current minimum, add to list
25            else if (curr_diff == min_diff) {
26                result.push_back({arr[i], arr[i+1]});
27            }
28        }
29        return result;
30    }
31};