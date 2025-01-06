"""
https://leetcode.cn/problems/valid-arrangement-of-pairs/
"""
from collections import defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        indeg = defaultdict(int)
        outdeg = defaultdict(int)
        g = defaultdict(list)
        for u, v in pairs:
            outdeg[u] += 1
            indeg[v] += 1
            g[u].append(v)

        stack = []

        def dfs(x):
            while g[x]:
                y = g[x].pop()
                dfs(y)
                stack.append(y)

        start = pairs[0][0]
        for i in g:
            if outdeg[i] - indeg[i] == 1:
                start = i

        dfs(start)
        stack = [start] + stack[::-1]
        ans = []
        for i, v in enumerate(stack[:-1]):
            ans.append([v, stack[i + 1]])
        return ans
