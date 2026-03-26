from itertools import accumulate


def main():
    n, m = map(int, input().split())
    mn = min(map(int, input().split()))
    mx = mn + n - 1
    d = [0] * (n + 10)
    mod = 10007
    for _ in range(m):
        l, r = map(int, input().split())
        l = max(l, mn) - mn
        r = min(r, mx) - mn
        if l >= n or r < 0:
            continue
        d[l] += 1
        d[r + 1] -= 1
    # print(d)
    pi = sum(accumulate(d)) % mod
    return (n * m % mod - pi) % mod


if __name__ == '__main__':
    ans = main()
    print(ans)
