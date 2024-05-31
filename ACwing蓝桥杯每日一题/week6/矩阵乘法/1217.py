"""
https://www.acwing.com/problem/content/1219/
"""
MOD = int(1e9 + 7)
op = {
    1: 4,
    4: 1,
    2: 5,
    5: 2,
    3: 6,
    6: 3
}


def dot(m1, m2):
    """m1,m2是6*6的矩阵"""
    res = [[0] * 6 for _ in range(6)]
    for i in range(0, 6):
        for j in range(0, 6):
            for k in range(0, 6):
                res[i][j] = (res[i][j] + m1[i][k] * m2[k][j]) % MOD
    return res


def quickMatrix(n):
    """矩阵快速幂"""
    if n == 1:
        return matrix
    if n % 2 == 0:
        a = quickMatrix(n // 2)
        return dot(a, a)
    else:
        a = quickMatrix(n - 1)
        return dot(a, matrix)


n, m = map(int, input().split(" "))
matrix = [[1] * 6 for _ in range(6)]
for _ in range(m):
    a, b = map(int, input().split(" "))
    matrix[a - 1][op[b] - 1] = 0
    matrix[b - 1][op[a] - 1] = 0
if n == 1:
    print(6)
    exit()
q = quickMatrix(n - 1)
ans = 0
for i in q:
    ans = (ans + sum(i)) % MOD
print((ans * pow(4, n, MOD)) % MOD)
