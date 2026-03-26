n, m, k = map(int, input().split(" "))
in_arr = [list(map(int, input().split(" "))) for _ in range(0, n)]
arr = [[0 for _ in range(0, m + 1)] for _ in range(0, n + 1)]
# 构造前缀和，按照列构造
for i in range(1, n + 1):
    for j in range(1, m + 1):
        arr[i][j] = in_arr[i - 1][j - 1] + arr[i - 1][j]
res = 0
for i in range(1, n + 1):
    for j in range(i, n + 1):
        l = 1
        sum = 0
        for r in range(1, m + 1):
            sum += arr[j][r] - arr[i - 1][r]
            while sum > k:
                sum -= arr[j][l] - arr[i - 1][l]
                l += 1
            res += r - l + 1
print(res)
