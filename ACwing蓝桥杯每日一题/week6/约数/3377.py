"""
https://www.acwing.com/problem/content/3380/
"""


def solve(n):
    if n == 1:
        return 1
    res = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            res.add(i)
            res.add(n // i)
        i += 1
    return len(res)


n = int(input())
lst = list(map(int, input().split(" ")))
res = [solve(i) for i in lst]
for i in res:
    print(i)
