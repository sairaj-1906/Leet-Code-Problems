1class Solution:
2    def readBinaryWatch(self, turnedOn: int) -> List[str]:
3        times = []
4        # Iterate through all possible hours and minutes
5        for h in range(12):
6            for m in range(60):
7                # Count bits in hour + bits in minute
8                # bin(3) -> '0b11', count('1') -> 2
9                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
10                    # Format: h is standard, m must be 2 digits with leading zero
11                    times.append(f"{h}:{m:02d}")
12        return times