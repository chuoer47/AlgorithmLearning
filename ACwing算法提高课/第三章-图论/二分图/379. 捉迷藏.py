"""
https://www.acwing.com/problem/content/description/381/

相关题解：https://blog.csdn.net/EQUINOX1/article/details/135631810
"""

match = []
visit = []


def find(x):
    for i, v in enumerate(link[x]):
        if v and not visit[i]:
            visit[i] = 1
            t = match[i]
            if not t or find(t):  # 经典条件
                match[i] = x
                return True
    return False


if __name__ == '__main__':
    n, m = map(int, input().strip().split(" "))
    link = [[0] * (n + 1) for _ in range(n + 1)]  # 链接矩阵,这里就相当于在拆点了
    match = [0] * (n + 1)  # 存取匹配结果
    for _ in range(m):
        a, b = map(int, input().strip().split(" "))
        link[a][b] = 1

    # 相当与Floyd算法，不过是找**闭包**
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                link[i][j] |= link[i][k] & link[k][j]

    ans = 0
    # 经典匈牙利算法
    for i in range(1, n + 1):
        visit = [0] * (n + 1)
        if find(i):
            ans += 1
    print(n - ans)
