# 能想出来个大概；
# 基本思想就是至少性滑动窗口 + 推公式；
# 公式比较难推理；数论知识

@cache
def helper(x):
    m = x.bit_length()
    ans = sum((i + 1) // 2 << (i - 1) for i in range(1, m)) # 累加<m位的操作数
    return ans + (m + 1) // 2 * (x + 1 - (1 << m >> 1)) # 计算m位最小的数到x的操作数

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        return sum((helper(r) - helper(l - 1) + 1) // 2 for l, r in queries)