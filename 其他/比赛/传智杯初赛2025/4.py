import bisect
from collections import defaultdict
from itertools import accumulate

n = int(input())
nums = []
cnt = defaultdict(int)

for _ in range(n):
    a, b = map(int, input().split(" "))
    if b > cnt[a]:
        cnt[a] = b
p = [(a, b) for a, b in cnt.items()]
p.sort()
nums = list(a for a, _ in p)
vals = list(b for _, b in p)
vals = list(accumulate(vals, func=max))

q = int(input())
for _ in range(q):
    x = int(input())
    idx = bisect.bisect_right(nums, x) - 1

    if idx >= 0:
        print(vals[idx])
    else:
        print(-1)
