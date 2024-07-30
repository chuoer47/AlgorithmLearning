"""
https://www.acwing.com/problem/content/7/

核心思想为转化为多重背包问题即可
"""

from collections import deque

if __name__ == '__main__':
    n, v = map(int, input().strip().split(" "))
    lst = [list(map(int, input().strip().split(" "))) for _ in range(n)]
    # 把lst预处理就好了
    for i in lst:
        if i[2]==-1:
            i[2]=1
        elif i[2]==0:
            i[2] = 1000
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