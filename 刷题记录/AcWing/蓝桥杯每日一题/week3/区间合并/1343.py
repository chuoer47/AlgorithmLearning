"""
https://www.acwing.com/problem/content/1345/
"""

n = int(input())
lst = [list(map(int, input().split(" "))) for i in range(n)]
lst.sort()
max_time = 0
max_no_time = 0
ll, rr = lst[0][0], lst[0][1]
# 计算区间重叠部分
for l, r in lst:
    if l <= rr:
        max_time = max(max(r, rr) - min(l, ll), max_time)
        ll, rr = min(l, ll), max(r, rr)
    else:
        max_time = max(r - l, rr - ll, max_time)
        max_no_time = max(l - rr, max_no_time)
        ll, rr = l, r
print(max_time, max_no_time)
