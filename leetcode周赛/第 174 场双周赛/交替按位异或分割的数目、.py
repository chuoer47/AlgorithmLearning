class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        # 线性DP + 异或前缀和
        mod = int(1e9 + 7)
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        mapper1 = defaultdict(int)
        mapper2 = defaultdict(int)
        mapper2[0] = 1
        pi = 0
        for i, v in enumerate(nums):
            pi ^= v
            dp[i][0] = mapper1[target2 ^ pi]
            dp[i][1] = mapper2[target1 ^ pi]
            mapper1[pi] = (mapper1[pi] + dp[i][1]) % mod
            mapper2[pi] = (mapper2[pi] + dp[i][0]) % mod
        return (dp[n - 1][0] + dp[n - 1][1]) % mod
