1class Solution:
2    def findMinArrowShots(self, points: List[List[int]]) -> int:
3        if not points:
4            return 0
5
6        points.sort(key=lambda x: x[1])
7
8        arrows = 1
9        current_end = points[0][1]
10
11        for i in range(1, len(points)):
12            if points[i][0] > current_end:
13                arrows += 1
14                current_end = points[i][1]
15
16        return arrows