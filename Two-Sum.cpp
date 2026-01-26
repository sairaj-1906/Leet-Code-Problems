1#include <vector>
2#include <unordered_map>
3
4class Solution {
5public:
6    std::vector<int> twoSum(std::vector<int>& nums, int target) {
7        // Map to store number and its index: {number: index}
8        std::unordered_map<int, int> map;
9
10        for (int i = 0; i < nums.size(); i++) {
11            int complement = target - nums[i];
12
13            // Check if the complement exists in the map
14            if (map.find(complement) != map.end()) {
15                // If found, return the index of the complement and the current index
16                return {map[complement], i};
17            }
18
19            // Otherwise, add the current number and index to the map
20            map[nums[i]] = i;
21        }
22
23        return {}; // Return empty if no solution found
24    }
25};