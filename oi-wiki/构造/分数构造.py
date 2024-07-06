"""
https://codeforces.com/problemset/problem/743/C
通过数学知识可以看出
n,n+1,n(n+1)为一个结构解
"""


def solve(n):
    return n, n + 1, n * (n + 1)


n = int(input())
print(solve(n))
