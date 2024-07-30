"""
https://www.acwing.com/problem/content/101/
"""
N = 5010  # 需要时修改
lst = [[0] * N for _ in range(N)]

if __name__ == '__main__':
    n, r = map(int, input().split(" "))
    r = min(r, 5001)  # 优化一下r
    if r == 0:
        """特判一下"""
        print(0)
        exit(1)
    # 数据录入
    for _ in range(n):
        x, y, w = map(int, input().split(" "))
        lst[x + 1][y + 1] += w  # 注意可叠加

    # 开始数据预处理，二维前缀和
    # 本来一开始想只预处理有数据的最大行和最大列
    # 但是由于滑动窗口可能有超出的情况，特判很麻烦，只能全部预处理
    for i in range(1, N):
        for j in range(1, N):
            lst[i][j] += lst[i - 1][j] + lst[i][j - 1] - lst[i - 1][j - 1]
            # print(i, j, lst[i][j])

    # 滑动窗口启动！ (i,j)表示为滑动窗口的左上角
    ans = 0
    for i in range(1, 5002 - r + 2):
        for j in range(1, 5002 - r + 2):
            ans = max(ans,
                      lst[i + r - 1][j + r - 1] - lst[i + r - 1][j - 1] - lst[i - 1][j + r - 1] + lst[i - 1][j - 1])

    print(ans)
