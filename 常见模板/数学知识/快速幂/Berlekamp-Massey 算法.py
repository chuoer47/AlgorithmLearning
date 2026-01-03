from typing import List

MOD = 1_000_000_007


class BerlekampMasseyKitamasa:
    """
    提供 Berlekamp-Massey 算法和 Kitamasa 算法的实现，
    用于求解线性递推数列的最短递推式以及快速计算第 n 项。
    """

    # Berlekamp-Massey 算法：给定数列前 m 项，返回最短常系数齐次线性递推式的系数
    # coef 的顺序为 [c1, c2, ..., ck]，满足 f(n) = c1*f(n-1) + c2*f(n-2) + ... + ck*f(n-k)
    def berlekampMassey(self, a: List[int]) -> List[int]:
        pre_c = []
        pre_i, pre_d = -1, 0
        coef = []

        for i, v in enumerate(a):
            # 计算误差 d = a[i] - sum(coef[j] * a[i-1-j])
            d = (v - sum(c * a[i - 1 - j] for j, c in enumerate(coef))) % MOD
            if d == 0:
                continue

            if pre_i < 0:
                coef = [0] * (i + 1)
                pre_i, pre_d = i, d
                continue

            bias = i - pre_i
            old_len = len(coef)
            new_len = bias + len(pre_c)
            if new_len > old_len:
                tmp = coef[:]
                coef += [0] * (new_len - old_len)

            delta = d * pow(pre_d, MOD - 2, MOD) % MOD
            coef[bias - 1] = (coef[bias - 1] + delta) % MOD
            for j, c in enumerate(pre_c):
                coef[bias + j] = (coef[bias + j] - delta * c) % MOD

            if new_len > old_len:
                pre_c = tmp
                pre_i, pre_d = i, d

        return coef

    # Kitamasa 算法：根据递推式 coef 和初始值 a，计算第 n 项 f(n) mod MOD
    # coef 的顺序为 [c1, c2, ..., ck]，满足 f(n) = c1*f(n-1) + c2*f(n-2) + ... + ck*f(n-k)
    def kitamasa(self, coef: List[int], a: List[int], n: int) -> int:
        if n < len(a):
            return a[n] % MOD

        k = len(coef)
        if k == 0:
            return 0
        if k == 1:
            return a[0] * pow(coef[0], n, MOD) % MOD

        # 辅助函数：compose(a, b) 用于状态转移的复合
        def compose(a_coeff: List[int], b_coeff: List[int]) -> List[int]:
            res = [0] * k
            temp = b_coeff.copy()
            for ac in a_coeff:
                for j in range(k):
                    res[j] = (res[j] + ac * temp[j]) % MOD
                # 更新 temp 为下一个状态
                bk1 = temp[-1]
                for j in range(k - 1, 0, -1):
                    temp[j] = (temp[j - 1] + bk1 * coef[j]) % MOD
                temp[0] = bk1 * coef[0] % MOD
            return res

        res_c = [0] * k
        c = [0] * k
        res_c[0] = 1
        c[1] = 1

        while n > 0:
            if n % 2 == 1:
                res_c = compose(c, res_c)
            c = compose(c, c.copy())
            n //= 2

        return sum(c * v for c, v in zip(res_c, a)) % MOD


if __name__ == "__main__":
    bmk = BerlekampMasseyKitamasa()

    # 示例：斐波那契数列
    fib = [0, 1, 1, 2, 3, 5, 8, 13]
    coef = bmk.berlekampMassey(fib)
    print("递推系数:", coef)  # 应该是 [1, 1]

    # 用 Kitamasa 求第 100 项
    print("第 100 项:", bmk.kitamasa(coef, fib, 100))
