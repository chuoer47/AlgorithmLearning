from _bisect import bisect_left
from typing import List


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # 最小最大:二分
        # 根据位置情况分类讨论
        n = len(points)

        def get_dis(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 3 * side - x
            else:
                return 4 * side - y

        def manha_dis(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        dis = [(get_dis(x, y), x, y) for x, y in points]
        dis.sort()
        keys = [x[0] for x in dis]


        def check(mid):
            # 给定mid：最大的距离；找出最多的最小距离>=mid 的点
            # 如果不是正方形，是直线就好求很多了，排序 + 二分寻找既可以
            ans = 0
            # 枚举起点咯？
            for i in range(n):
                nx = i
                flag = True
                for _ in range(k-1):
                    nd = dis[nx][0] + mid
                    idx = bisect_left(keys, nd)  # dis[idx][0] >= nx
                    if idx >= n:
                        flag = False
                        continue
                    nx = idx
                if flag and manha_dis(dis[i][1], dis[i][2], dis[nx][1], dis[nx][2]) >= mid:
                    return True
            return False

        l, r = 0, side
        ans = -1
        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                ans = max(mid, ans)
                l = mid + 1
            else:
                r = mid - 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxDistance(side=2, points=[[0, 2], [2, 0], [2, 2], [0, 0]], k=4))
