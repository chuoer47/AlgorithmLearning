from math import ceil


class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        # 确定一个点，以该点为中心组成的半个边长为k的正方形不用标记
        # 应该可以使用数学方法解决
        k = 1 + 2 * k
        return ceil(n / k) * ceil(m / k)
