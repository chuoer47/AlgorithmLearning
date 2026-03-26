n, m, k = map(int, input().split(" "))
in_arr = [list(map(int, input().split(" "))) for _ in range(0, n)]
arr = [[0 for _ in range(0, m + 1)] for _ in range(0, n + 1)]  # 前缀和
for i in range(1, n + 1):
    for j in range(1, m + 1):
        arr[i][j] = in_arr[i - 1][j - 1] + arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]
res = 0
record = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if in_arr[i - 1][j - 1] <= k:
            for ii in range(1, i + 1):
                for jj in range(1, j + 1):
                    tem = arr[i][j] - arr[ii - 1][j] - arr[i][jj - 1] + arr[ii - 1][jj - 1]
                    if tem <= k:
                        record.append(list([ii, jj, i, j]))
                        res += 1
print(res)
