"""
https://www.acwing.com/problem/content/description/4968/
"""

n = int(input())
a = list(map(int, input().strip().split(" ")))
b = list(map(int, input().strip().split(" ")))
c = list(map(int, input().strip().split(" ")))


def getMax(a, b, c):
    t = [a[i] - b[i] - c[i] for i in range(n)]
    t.sort(reverse=True)
    res = 0
    for i in range(n):
        res += t[i]
        if res <= 0:
            return i
    return n


res = max(getMax(a, b, c),
          getMax(b, a, c),
          getMax(c, b, a))
if res:
    print(res)
else:
    print(-1)
