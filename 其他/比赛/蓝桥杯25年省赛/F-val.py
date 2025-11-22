import random
from bisect import bisect_left
from random import randint


def simple(n, nums):
    # 贪心取答案
    nums = list(map(str, nums))
    nums = [x.count("6") for x in nums]
    print(sorted(nums))
    nxt = []
    ans = 0
    # 贪心取1
    for x in nums:
        if x >= 6:
            ans += 1
        else:
            nxt.append(x)
    # 贪心取2
    nnxt = []
    nxt.sort()
    while nxt:
        now = nxt.pop()
        idx = bisect_left(nxt, 6 - now)  # nxt[idx] + now >= 6 => nxt[idx] >= 6 - now
        if nxt and idx < len(nxt) and nxt[idx] + now >= 6:
            nxt.pop(idx)
            ans += 1
        else:
            nnxt.append(now)
    # 贪心取3
    nxt = nnxt
    nxt.sort()
    while len(nxt) > 2:
        x, y = nxt.pop(), nxt.pop(),
        now = x + y
        idx = bisect_left(nxt, 6 - now)  # nxt[idx] + now >= 6 => nxt[idx] >= 6 - now
        if nxt and idx < len(nxt) and nxt[idx] + now >= 6:
            nxt.pop(idx)
            ans += 1

    return ans


for _ in range(10):

    n = randint(1, 1000)
    nums = []
    for i in range(n):
        nums.append(3 * "6")
    print(n, nums)
    print(simple(n, nums))
