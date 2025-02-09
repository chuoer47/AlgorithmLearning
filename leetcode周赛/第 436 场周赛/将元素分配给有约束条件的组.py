from cmath import inf, sqrt
from collections import defaultdict
from typing import List


class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        n = len(groups)
        ans = [inf] * n
        idx = defaultdict(lambda: inf)
        for i, v in enumerate(elements):
            idx[i] = min(idx[i], v)
        for i in range(n):
            var = groups[i]
            for j in range(1, int(sqrt(var)) + 2):
                if var % j == 0:
                    ans[i] = min(ans[i], idx[j], idx[var // j])
            if ans[i] == inf:
                ans[i] = -1
        return ans
