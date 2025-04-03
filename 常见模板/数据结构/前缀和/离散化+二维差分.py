"""
LCP 74. 最强祝福力场
"""
from typing import List


class Solution:
    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:
        # 离散化+差分（太离谱了，这也能）

        forceField = [(2 * i, 2 * j, e) for i, j, e in forceField]  # 乘2预处理避免小数
        # 离散化 + 坐标映射
        x_set = set()
        y_set = set()
        for i, j, e in forceField:
            x_set.add(i - e)
            x_set.add(i + e)
            y_set.add(j - e)
            y_set.add(j + e)
        xs = sorted(x_set)
        ys = sorted(y_set)
        x_mapper = {v: i for i, v in enumerate(xs)}
        y_mapper = {v: i for i, v in enumerate(ys)}
        n, m = len(xs), len(ys)
        # 建立差分数组
        diff = [[0] * (m + 2) for _ in range(n + 2)]
        for i, j, e in forceField:
            row1, col1, row2, col2 = (
                x_mapper[i - e],
                y_mapper[j - e],
                x_mapper[i + e],
                y_mapper[j + e],
            )
            diff[row1][col1] += 1
            diff[row1][col2 + 1] -= 1
            diff[row2 + 1][col1] -= 1
            diff[row2 + 1][col2 + 1] += 1
        # 利用差分数组还原
        for i in range(n):
            for j in range(m):
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
        # 输出答案
        return max(map(max, diff))
