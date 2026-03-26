"""
https://www.acwing.com/problem/content/1223/
暴力解法
"""
from math import sqrt


def solve(n):
    global res
    for d in range(int(sqrt(n)), -1, -1):
        t1 = n - d * d
        if t1 == 0:
            res = [0, 0, 0, d]  # 绝对选取这种情况
            return
        for c in range(int(sqrt(t1)), -1, -1):
            t2 = t1 - c * c
            if t2 == 0:
                t = [res, [0, 0, c, d]]
                t.sort()
                res = t[0]
                continue
            for b in range(int(sqrt(t2)), -1, -1):
                t3 = t2 - b * b
                if t3 == 0:
                    t = [res, [0, b, c, d]]
                    t.sort()
                    res = t[0]
                    continue
                for a in range(int(sqrt(t3)), -1, -1):
                    t4 = t3 - a * a
                    if t4 == 0:
                        t = [res, [a, b, c, d]]
                        t.sort()
                        res = t[0]
                        continue


n = int(input())
res = [n,n,n,n]
solve(n)
print(*res)
