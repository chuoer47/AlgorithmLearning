"""
采用滚动数组+单调队列的方式优化时间复杂度

参考：
https://www.acwing.com/activity/content/code/content/2662492/

通过了 14/16个数据 TLE
"""
from collections import deque

if __name__ == '__main__':
    n, v = map(int, input().strip().split(" "))
    lst = [list(map(int, input().strip().split(" "))) for _ in range(n)]
    dp = [0] * (v + 10)
    for i in range(0, n):  # 枚举物品
        vi, wi, si = lst[i]
        pre = dp.copy()
        for r in range(0, vi):  # 枚举余数
            q = deque()  # 使用单调队列维护从高到低的顺序，存储的值为下标
            for j in range(r, v + 1, vi):  # 枚举背包空间，按照vi为间隔
                while q and (j - q[0]) // vi > si:  # 弹出不在滑动窗口的值
                    q.popleft()
                while q and pre[q[-1]] - (q[-1] - r) // vi * wi <= pre[j] - (j - r) // vi * wi:
                    q.pop()
                q.append(j)
                dp[j] = max(dp[j], pre[q[0]] + (j - q[0]) // vi * wi)
    print(dp[v])

"""
下面是优化常数过来的代码！

from collections import deque

if __name__ == '__main__':
    n, v = map(int, input().strip().split(" "))
    lst = [list(map(int, input().strip().split(" "))) for _ in range(n)]
    dp = [0] * (v + 10)
    for i in range(0, n):  # 枚举物品
        vi, wi, si = lst[i]
        pre = dp.copy()
        for r in range(0, vi):  # 枚举余数
            q = deque()  # 使用单调队列维护从高到低的顺序，存储的值为下标
            for j in range(r, v + 1, vi):  # 枚举背包空间，按照vi为间隔
                while q and (j - q[0]) > vi * si:  # 弹出不在滑动窗口的值
                    q.popleft()
                while q and pre[q[-1]] + (j - q[-1])//vi * wi <= pre[j]:
                    q.pop()
                q.append(j)
                dp[j] = max(dp[j],pre[q[0]]+(j-q[0])//vi*wi)
    print(dp[v])


"""
