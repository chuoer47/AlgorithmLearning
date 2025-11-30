class SOSDP:
    def __init__(self, n):
        """n = 比特数（数组大小为 2^n）"""
        self.n = n
        self.N = 1 << n
        self.f = [0] * self.N

    def sos_subset(self):
        """子集和 DP: f[mask] += f[mask_without_bit_i]"""
        for i in range(self.n):
            bit = 1 << i
            for mask in range(self.N):
                if mask & bit:
                    self.f[mask] += self.f[mask ^ bit]

    def sos_superset(self):
        """超集和 DP: f[mask] += f[mask_with_bit_i]"""
        for i in range(self.n):
            bit = 1 << i
            for mask in range(self.N):
                if not (mask & bit):
                    self.f[mask] += self.f[mask | bit]

if __name__ == '__main__':
    n = 5
    dp = SOSDP(n)

    # 初始化 f
    for mask in range(dp.N):
        dp.f[mask] = mask  # 示例：f[mask] = mask 本身

    dp.sos_subset()

    print(dp.f)