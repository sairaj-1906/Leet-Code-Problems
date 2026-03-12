1class Solution:
2    def hIndex(self, citations: List[int]) -> int:
3        # Sort citations in decending order
4        citations.sort(reverse = True)
5        h = 0
6        for i, c in enumerate(citations):
7            # i + 1 represents the number of papers we've looked at so far
8            if c >= i + 1:
9                h = i + 1
10            else:
11                break
12        return h