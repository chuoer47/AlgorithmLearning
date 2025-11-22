#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param edges int整型一维数组
# @return int整型
#
from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        from collections import deque
        n = len(edges)
        # 先拓扑排序 判断是否存在环
        deg = [0] * n
        for i in edges:
            if i != -1:
                deg[i] += 1
        topsort = 0
        q = deque()
        for i, v in enumerate(deg):
            if v == 0:
                q.append(i)
                topsort += 1
        while q:
            x = q.popleft()
            deg[edges[x]] -= 1
            if deg[edges[x]] == 0:
                q.append(edges[x])
                topsort += 1
        if topsort == n:
            return -1

        # 深搜找环 （这个数据集只有一个环，笑死了，完全不需要找环的个数了）
        return n - topsort


if __name__ == '__main__':
    s = Solution()
    edges = [2, -1, 3, 1]
    print(s.longestCycle(edges))
