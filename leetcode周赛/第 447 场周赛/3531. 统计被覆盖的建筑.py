from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        col = defaultdict(list)
        row = defaultdict(list)
        for x, y in buildings:
            row[x].append(y)
            col[y].append(x)
        for x in col.values():
            x.sort()
        for x in row.values():
            x.sort()
        ans = 0

        def check(x, y):
            r = row[x]
            idx = bisect_left(r, y)
            if idx == 0 or idx == len(r) - 1:
                return False
            c = col[y]
            idx = bisect_left(c, x)
            if idx == 0 or idx == len(c) - 1:
                return False
            return True

        for x, y in buildings:
            if check(x, y):
                ans += 1
        return ans
