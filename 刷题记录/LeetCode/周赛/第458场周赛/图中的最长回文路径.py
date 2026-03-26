from functools import cache
from typing import List

max1 = lambda x, y: x if x > y else y


class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = 0

        @cache
        def backtrack(left: int, right: int, mask: int):
            # n*n*2^n*n*n = 6e8
            nonlocal ans
            # print(left, right, bin(mask))
            ans = max1(ans, bin(mask).count('1'))
            for l in g[left]:
                for r in g[right]:
                    if (mask & (1 << l) == 0) and (mask & (1 << r) == 0) and l != r and label[l] == label[r]:
                        # 剪枝
                        if l > r:
                            l, r = r, l
                        backtrack(l, r, mask | (1 << l) | (1 << r))

        # 奇数
        for i in range(n):
            backtrack(i, i, 1 << i)
        # 偶数
        for x, y in edges:
            if label[x] == label[y]:
                if x > y:
                    x, y = y, x
                backtrack(x, y, (1 << x) | (1 << y))
        backtrack.cache_clear()

        return ans

