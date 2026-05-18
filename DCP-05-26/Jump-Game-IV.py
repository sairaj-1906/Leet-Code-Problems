1from collections import defaultdict, deque
2from typing import List
3
4class Solution:
5    def minJumps(self, arr: List[int]) -> int:
6        n = len(arr)
7        if n <= 1:
8            return 0
9
10        graph = defaultdict(list)
11        for i, val in enumerate(arr):
12            graph[val].append(i)
13            
14        queue = deque([0])
15        visited = {0}
16        steps = 0
17        
18        while queue:
19            for _ in range(len(queue)):
20                node = queue.popleft()
21
22                if node == n - 1:
23                    return steps
24                
25                for child in graph[arr[node]]:
26                    if child not in visited:
27                        visited.add(child)
28                        queue.append(child)
29                        
30                graph[arr[node]].clear()
31                
32                for child in (node-1, node+1):
33                    if 0 <= child < n and child not in visited:
34                        visited.add(child)
35                        queue.append(child)
36            
37            steps += 1
38            
39        return -1