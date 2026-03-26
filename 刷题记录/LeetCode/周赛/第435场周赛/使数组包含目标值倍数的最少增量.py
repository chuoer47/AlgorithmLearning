class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        # target去重
        target = list(set(target))
        n, m = len(nums), len(target)

        # 预处理target相互之间的公倍数
        pi = [0] * (1 << m)
        for i in range(1 << m):
            tmp = 1
            for j in range(m):
                if (i >> j) & 1:
                    tmp = math.lcm(tmp, target[j])
            pi[i] = tmp

        def get(var, fac):
            if var % fac == 0:
                return 0
            return abs(var - (var // fac + 1) * fac)

        # dp[i][j] 表示前i个,状态压缩j（对应倍数情况），最少操作数
        dp = [[inf] * (1 << m) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
        for i in range(1, n + 1):
            var = nums[i - 1]
            for j in range(1 << m):
                # 遍历子集的模板
                k = j
                while True:
                    fac = pi[k]
                    dp[i][j] = min(dp[i][j], dp[i - 1][j], dp[i - 1][j - k] + get(var, fac))

                    k = (k - 1) & j
                    if k == j:
                        break

        return dp[i][(1 << m) - 1]
