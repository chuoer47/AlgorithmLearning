"""
https://www.acwing.com/problem/content/description/1357/
"""


def bfs(lst):
    a, b, c = lst
    if lst in use:
        return
    use.add((a, b, c))
    ra = A - a
    rb = B - b
    rc = C - c
    if a != 0:
        state.append((a - min(a, rb), b + min(a, rb), c))
        state.append((a - min(a, rc), b, c + min(a, rc)))
    if b != 0:
        state.append((a + min(b, ra), b - min(b, ra), c))
        state.append((a, b - min(b, rc), c + min(b, rc)))
    if c != 0:
        state.append((a + min(c, ra), b, c - min(c, ra)))
        state.append((a, b + min(c, rb), c - min(c, rb)))


A, B, C = map(int, input().split(" "))
use = set()
state = [(0, 0, C)]
while state:
    lst = state.pop()
    # print(lst)
    bfs(lst)
# print(use)
res = []
for a, b, c in use:
    if a == 0:
        res.append(c)
res.sort()
res = set(res)
print(*res)
