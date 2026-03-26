import random
from itertools import accumulate


def main(n, mn, ops):
    mx = mn + n - 1
    d = [0] * (n + 10)
    mod = 10007
    for l, r in ops:
        l = max(l, mn) - mn
        r = min(r, mx) - mn
        if l >= n:
            continue
        d[l] += 1
        d[r + 1] -= 1
    # print(d)
    pi = sum(accumulate(d)) % mod
    return (n * len(ops) % mod - pi) % mod


def baoli(nums, ops):
    ans = 0
    for l, r in ops:
        for x in nums:
            if not l <= x <= r:
                ans += 1
    return ans % 10007


if __name__ == '__main__':
    n = 10000
    nums = list(range(1, n + 1))
    ops = []
    for _ in range(99):
        l = random.randint(1, int(1e9))
        r = random.randint(1, int(1e9))
        if l <= r:
            ops.append([l, r])
    # ops = [[1, 1000], [5, 77], [9, 444444]]
    print(main(n, 1, ops))
    print(baoli(nums, ops))
