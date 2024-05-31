"""
https://www.acwing.com/problem/content/207/
"""
import sys

sys.setrecursionlimit(100000)
MOD = 10000
matrix = [[0, 1], [1, 1]]


def dot(m1, m2):
    lst = [[0, 0], [0, 0]]
    lst[0][0] = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % MOD
    lst[0][1] = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % MOD
    lst[1][0] = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % MOD
    lst[1][1] = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % MOD
    return lst


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


while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        print(0)
        continue
    m = quickMatrix(n)
    print(m[1][0])
