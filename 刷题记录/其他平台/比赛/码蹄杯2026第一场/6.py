mod = int(1e9 + 7)


def comb_init(N, mod):
    fac = [1] * (N + 1)
    for i in range(1, N + 1):
        fac[i] = fac[i - 1] * i % mod
    ifac = [1] * (N + 1)
    ifac[N] = pow(fac[N], mod - 2, mod)
    for i in range(N, 0, -1):
        ifac[i - 1] = ifac[i] * i % mod

    def C(n, k):
        if k < 0 or k > n:
            return 0
        return fac[n] * ifac[k] % mod * ifac[n - k] % mod

    return C


if __name__ == '__main__':
    n = int(input())
    s = input()
    cnt1 = s.count('1')
    cnt0 = n - cnt1
    C = comb_init(n, mod)
    # 本质上就是统计能构成的，不同的独特的字符串与原串 直接不同的位置的数量
    # 统计差1个，差2个等等等的情况...
    # 假设差1个，从 comb(cnt1,1) * comb(cnt0,1) ....
    # 以此类推即可
    # 需要一个comb + mod的模板
    ans = 0
    for i in range(1, min(cnt0, cnt1) + 1):
        print(i)
        ans = (ans + i * C(cnt0, i) * C(cnt1, i)) % mod
    print(ans)
