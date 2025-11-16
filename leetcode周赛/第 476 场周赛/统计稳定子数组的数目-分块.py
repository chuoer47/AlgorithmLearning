from math import isqrt
from typing import List
from sortedcontainers import SortedList

from math import isqrt
from typing import List
from sortedcontainers import SortedList


class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(nums), len(queries)
        B = isqrt(n) + 1
        q = len(queries)
        if n == 0:
            return [0] * q
        queries = [(l, r, i) for i, (l, r) in enumerate(queries)]

        def mo_cmp(query):
            # 经典优化操作
            # 排序查询：按左端点块号，奇块升序右，偶块降序右
            L, R, _ = query
            block = L // B
            return (block, R if block % 2 == 0 else -R)

        queries.sort(key=mo_cmp)

        # 预处理以免暴力搜索
        lpi = [0] * n
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                lpi[i] = lpi[i - 1]
            else:
                lpi[i] = i

        rpi = [0] * n
        rpi[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                rpi[i] = rpi[i + 1]
            else:
                rpi[i] = i

        ans = [0] * q
        curL = 0
        curR = -1
        res = 0

        # 右指针右移：新增以curR为终点的稳定子数组
        def expand_right():
            nonlocal curR, res, curL
            curR += 1
            j = max(lpi[curR], curL)
            res += curR - j + 1

        # 右指针左移：减去以curR为终点的稳定子数组
        def shrink_right():
            nonlocal curR, res, curL
            j = max(lpi[curR], curL)
            res -= curR - j + 1
            curR -= 1

        # 左指针左移：新增以curL为起点的稳定子数组
        def expand_left():
            nonlocal curL, res, curR
            curL -= 1
            r = min(rpi[curL], curR)
            res += r - curL + 1

        # 左指针右移：减去以curL为起点的稳定子数组
        def shrink_left():
            nonlocal curL, res, curR
            r = min(rpi[curL], curR)
            res -= r - curL + 1
            curL += 1

        for L, R, idx in queries:
            # 移动到[L, R]
            while curR < R:
                expand_right()
            while curR > R:
                shrink_right()
            while curL > L:
                expand_left()
            while curL < L:
                shrink_left()
            ans[idx] = res

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countStableSubarrays(nums=[3, 1, 2], queries=[[0, 1], [1, 2], [0, 2]]))
    print(s.countStableSubarrays(nums=[2, 2], queries=[[0, 1], [0, 0]]))
