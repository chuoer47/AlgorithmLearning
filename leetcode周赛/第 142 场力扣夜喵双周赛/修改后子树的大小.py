from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(s)
        ans = [0] * n
        ano_parent = [-1] * n
        for i in range(1, n):
            now = parent[i]
            now_char = s[i]
            while parent[now] != -1 and s[now] != now_char:
                now = parent[now]
            if s[now] == now_char:
                ano_parent[i] = now
            else:
                ano_parent[i] = parent[i]
        parent = ano_parent
        for i in range(n):
            now = i
            while parent[now] != -1:
                ans[now] += 1
                now = parent[now]
            ans[now] += 1
        return ans
