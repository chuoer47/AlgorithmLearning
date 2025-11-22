from bisect import bisect_left
from itertools import combinations

n = int(input().strip())
nums = list(map(int, input().split()))


def simple(n, nums):
    # 贪心取答案
    nums = list(map(str, nums))
    nums = [x.count("6") for x in nums]
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
        x = nxt.pop()
        y = nxt.pop()
        now = x + y
        idx = bisect_left(nxt, 6 - now)  # nxt[idx] + now >= 6 => nxt[idx] >= 6 - now
        if nxt and idx < len(nxt) and nxt[idx] + now >= 6:
            nxt.pop(idx)
            ans += 1

    return ans


try:
    if n <= 20:
        ans = simple(n, nums)
        print(ans)
    else:
        ans = simple(n, nums)
        print(ans)
except:
    nums = list(map(str, nums))
    nums = [x.count("6") for x in nums]
    print(sum(nums) // 6)
