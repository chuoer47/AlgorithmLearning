"""
https://www.acwing.com/problem/content/424/
"""

l, m = map(int, input().split(" "))
lst = [list(map(int, input().split(" "))) for _ in range(m)]
lst.sort()
res = l + 1
ll, rr = lst[0][0], lst[0][1]
for l, r in lst:
    if l <= rr and r <= rr:
        continue
    elif l <= rr < r:
        rr = r
    elif l > rr:
        res -= rr - ll + 1
        ll, rr = l, r
res -= rr - ll + 1
print(res)