from bisect import bisect_left, bisect_right
from itertools import accumulate
from typing import List

MOD = 10 ** 9 + 7
n = int(1e5)
pow10 = [1] * (n + 1)
for k in range(1, n + 1):
    pow10[k] = (pow10[k - 1] * 10) % MOD


class PrefixSum:
    """前缀和工具类，用于快速计算区间和"""

    def __init__(self, values: List[int]):
        self.prefix = list(accumulate(values))  # 前缀和数组

    def get_range_sum(self, l: int, r: int) -> int:
        """获取区间 [l, r] 的和（0-based 闭区间），结果模 MOD"""
        if l > r:
            return 0
        total = self.prefix[r] if l == 0 else self.prefix[r] - self.prefix[l - 1]
        return total % MOD


class ConcatenateNum:
    """数字拼接工具类，用于快速计算区间数字拼接结果"""

    def __init__(self, values: List[int]):
        # 前缀拼接数组：prefix[i] = values[0..i] 拼接的数字 mod MOD
        self.prefix = list(accumulate(values, lambda x, y: (x * 10 + y) % MOD))

    def get_concat_result(self, l: int, r: int) -> int:
        """获取区间 [l, r] 数字拼接结果（0-based 闭区间），结果模 MOD"""
        if l > r:
            return 0
        if l == 0:
            return self.prefix[r]
        length = r - l + 1
        # 核心公式：拼接结果 = 整体前缀[r] - 前缀[l-1] * 10^长度（消除前缀影响）
        return (self.prefix[r] - self.prefix[l - 1] * pow10[length]) % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        # 过滤非0字符，记录其原始索引和数值
        non_zero_idx = []
        non_zero_vals = []
        for idx, c in enumerate(s):
            num = int(c)
            if num != 0:
                non_zero_idx.append(idx)
                non_zero_vals.append(num)

        # 初始化工具类
        prefix_sum = PrefixSum(non_zero_vals)
        concat_num = ConcatenateNum(non_zero_vals)

        ans = []
        for l, r in queries:
            # 找到查询区间 [l, r] 对应的非0数值区间（在non_zero_idx中的左右边界）
            left = bisect_left(non_zero_idx, l)
            right = bisect_right(non_zero_idx, r) - 1

            if left > right:
                ans.append(0)
                continue

            # 计算区间和 与 拼接结果 的乘积
            sum_val = prefix_sum.get_range_sum(left, right)
            concat_val = concat_num.get_concat_result(left, right)
            ans.append(sum_val * concat_val % MOD)

        return ans