1#include <vector>
2#include <string>
3#include <algorithm>
4
5using namespace std;
6
7class Solution {
8public:
9    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
10        // Initialize a 26x26 distance matrix with a large value (infinity)
11        // We use a large enough long long to avoid overflow during addition
12        const long long INF = 1e15;
13        vector<vector<long long>> dist(26, vector<long long>(26, INF));
14
15        // Distance to self is always 0
16        for (int i = 0; i < 26; ++i) {
17            dist[i][i] = 0;
18        }
19
20        // Fill the matrix with given transformation costs
21        for (int i = 0; i < original.size(); ++i) {
22            int u = original[i] - 'a';
23            int v = changed[i] - 'a';
24            dist[u][v] = min(dist[u][v], (long long)cost[i]);
25        }
26
27        // Floyd-Warshall Algorithm to find all-pairs shortest paths
28        for (int k = 0; k < 26; ++k) {
29            for (int i = 0; i < 26; ++i) {
30                for (int j = 0; j < 26; ++j) {
31                    if (dist[i][k] < INF && dist[k][j] < INF) {
32                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
33                    }
34                }
35            }
36        }
37
38        long long totalCost = 0;
39        int n = source.length();
40
41        // Calculate the total cost for the entire string
42        for (int i = 0; i < n; ++i) {
43            if (source[i] == target[i]) continue;
44
45            int u = source[i] - 'a';
46            int v = target[i] - 'a';
47
48            if (dist[u][v] >= INF) {
49                return -1; // Transformation impossible
50            }
51            totalCost += dist[u][v];
52        }
53
54        return totalCost;
55    }
56};