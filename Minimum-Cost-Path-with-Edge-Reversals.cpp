1#include <vector>
2#include <queue>
3#include <tuple>
4#include <algorithm>
5using namespace std;
6class Solution {
7public:
8    long long minCost(int n, vector<vector<int>>& edges) 
9    {
10        //Adjacency list: adj[u] contains{v, weight}
11        vector<vector<pair<int, int>>> adj(n);
12
13        for (const auto& edge : edges) 
14        {
15            int u = edge[0];
16            int v = edge[1];
17            int w = edge[2];
18            // 1. Normal traversal: u -> v with cost w
19            adj[u].push_back({v, w});
20            // 2. Switch traversal: v -> u with cost 2*w
21            // (Arrive at v, reverse incoming u->v, traverse to u)
22            adj[v].push_back({u, 2 * w});
23        }
24        // Dijkstra's Algorithm
25        // Min-priority queue storing {current_cost, u}
26        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
27        //Distance vector initialized to infinity
28        const long long INF = 1e18;
29        vector<long long> dist(n, INF);
30        dist[0] = 0;
31        pq.push({0,0});
32
33        while (!pq.empty())
34        {
35            long long d = pq.top().first;
36            int u = pq.top().second;
37            pq.pop();
38            //If we found a shorter path to u already, skip
39            if (d > dist[u]) continue;
40            //Optimization: If we reached target, return the cost
41            if (u == n-1) return d;
42
43            for(auto& edge : adj[u])
44            {
45                int v = edge.first;
46                int weight = edge.second;
47                
48                if (dist[u] + weight < dist[v])
49                {
50                    dist[v] = dist[u] + weight;
51                    pq.push({dist[v], v});
52                }
53            }
54        }
55        //If dist[n-1] is still INF, destination is unreachable
56        return (dist[n-1] == INF) ? -1 : dist[n-1];
57    }
58};