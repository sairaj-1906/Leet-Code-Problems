1import java.util.*;
2
3class Solution {
4    class DSU {
5        int[] parent;
6        int[] size;
7        int components;
8
9        public DSU(int n) {
10            parent = new int[n];
11            size = new int[n];
12            for (int i = 0; i < n; i++) {
13                parent[i] = i;
14                size[i] = 1;
15            }
16            components = n;
17        }
18
19        public int find(int i) {
20            if (parent[i] == i) return i;
21            return parent[i] = find(parent[i]); // Path compression
22        }
23
24        public boolean union(int i, int j) {
25            int rootI = find(i);
26            int rootJ = find(j);
27            if (rootI != rootJ) {
28                // Union by size
29                if (size[rootI] < size[rootJ]) {
30                    parent[rootI] = rootJ;
31                    size[rootJ] += size[rootI];
32                } else {
33                    parent[rootJ] = rootI;
34                    size[rootI] += size[rootJ];
35                }
36                components--;
37                return true;
38            }
39            return false;
40        }
41
42        // Fast clone to reuse the base state in our binary search
43        public DSU cloneDSU() {
44            DSU clone = new DSU(parent.length);
45            System.arraycopy(this.parent, 0, clone.parent, 0, parent.length);
46            System.arraycopy(this.size, 0, clone.size, 0, size.length);
47            clone.components = this.components;
48            return clone;
49        }
50    }
51
52    public int maxStability(int n, int[][] edges, int k) {
53        DSU dsuMust = new DSU(n);
54        DSU dsuAll = new DSU(n);
55        List<int[]> optional = new ArrayList<>();
56        
57        long minMustStrength = Long.MAX_VALUE;
58        long maxOptDoubled = 0;
59
60        for (int[] e : edges) {
61            dsuAll.union(e[0], e[1]);
62            
63            if (e[3] == 1) { // Mandatory edge
64                if (!dsuMust.union(e[0], e[1])) {
65                    // Mandatory edges form a cycle, spanning tree is impossible
66                    return -1;
67                }
68                minMustStrength = Math.min(minMustStrength, e[2]);
69            } else { // Optional edge
70                optional.add(e);
71                maxOptDoubled = Math.max(maxOptDoubled, e[2] * 2L);
72            }
73        }
74
75        // If the graph is inherently disconnected, return -1
76        if (dsuAll.components > 1) {
77            return -1;
78        }
79
80        long low = 1;
81        // The highest possible stability is bottlenecked by the weakest mandatory edge
82        long high = minMustStrength == Long.MAX_VALUE ? maxOptDoubled : minMustStrength;
83        long ans = -1;
84
85        while (low <= high) {
86            long mid = low + (high - low) / 2;
87            
88            if (check(mid, dsuMust, optional, k)) {
89                ans = mid;
90                low = mid + 1; // Valid stability, try to find a higher one
91            } else {
92                high = mid - 1; // Stability too high, scale it down
93            }
94        }
95
96        return (int) ans;
97    }
98
99    private boolean check(long X, DSU dsuMust, List<int[]> optional, int k) {
100        DSU dsu = dsuMust.cloneDSU();
101        int upgrades = 0;
102
103        // Phase 0: Add all optional edges that naturally satisfy the target stability X
104        for (int[] e : optional) {
105            if (e[2] >= X) {
106                dsu.union(e[0], e[1]);
107            }
108        }
109
110        // If Phase 0 alone connects the graph, it's valid
111        if (dsu.components == 1) {
112            return true;
113        }
114
115        // Phase 1: Add optional edges that need an upgrade to satisfy stability X
116        for (int[] e : optional) {
117            if (e[2] < X && e[2] * 2L >= X) {
118                // Ensure the edge actually connects distinct components before spending an upgrade
119                if (dsu.find(e[0]) != dsu.find(e[1])) {
120                    if (upgrades < k) {
121                        dsu.union(e[0], e[1]);
122                        upgrades++;
123                    }
124                }
125            }
126        }
127
128        return dsu.components == 1;
129    }
130}