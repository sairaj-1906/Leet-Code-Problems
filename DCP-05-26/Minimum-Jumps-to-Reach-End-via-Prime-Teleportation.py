1from collections import deque, defaultdict
2import math
3
4class Solution:
5    def minJumps(self, nums):
6        n = len(nums)
7
8        def is_prime(x):
9            if x < 2:
10                return False
11            if x == 2:
12                return True
13            if x % 2 == 0:
14                return False
15
16            limit = int(math.sqrt(x)) + 1
17            for i in range(3, limit, 2):
18                if x % i == 0:
19                    return False
20            return True
21
22        divisible = defaultdict(list)
23
24        for idx, num in enumerate(nums):
25            temp = num
26            d = 2
27
28            while d * d <= temp:
29                if temp % d == 0:
30                    divisible[d].append(idx)
31
32                    while temp % d == 0:
33                        temp //= d
34                d += 1
35
36            if temp > 1:
37                divisible[temp].append(idx)
38
39        q = deque([0])
40        visited = [False] * n
41        visited[0] = True
42
43        used_prime = set()
44
45        steps = 0
46
47        while q:
48            for _ in range(len(q)):
49                i = q.popleft()
50
51                if i == n - 1:
52                    return steps
53
54                for ni in [i - 1, i + 1]:
55                    if 0 <= ni < n and not visited[ni]:
56                        visited[ni] = True
57                        q.append(ni)
58
59                if is_prime(nums[i]):
60                    p = nums[i]
61
62                    if p not in used_prime:
63                        for ni in divisible[p]:
64                            if ni != i and not visited[ni]:
65                                visited[ni] = True
66                                q.append(ni)
67
68                        used_prime.add(p)
69
70            steps += 1
71
72        return -1