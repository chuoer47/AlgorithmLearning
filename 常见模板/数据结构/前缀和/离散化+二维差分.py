from typing import List


class Solution:
    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:
        """
        解决LCP 74. 最强祝福力场问题
        
        问题描述：每个祝福力场是一个以(i,j)为中心、边长为2e的正方形区域（即从(i-e,j-e)到(i+e,j+e)）。
        计算所有力场覆盖区域中，被覆盖次数最多的点的覆盖次数（即最大重叠次数）。
        
        解法思路：采用离散化+二维差分技术，高效处理大范围坐标下的区域覆盖计数问题
        """
        # 预处理：将坐标乘以2，避免计算过程中出现小数（因e为整数，乘2后所有边界均为整数）
        # 每个力场表示为(2i, 2j, e)，此时力场范围为[2i-e, 2i+e] × [2j-e, 2j+e]
        forceField = [(2 * i, 2 * j, e) for i, j, e in forceField]
        
        # 离散化：收集所有力场的边界坐标（x和y方向），用于映射到紧凑索引
        x_set = set()  # 存储x方向所有边界（左边界i-e和右边界i+e）
        y_set = set()  # 存储y方向所有边界（下边界j-e和上边界j+e）
        for i, j, e in forceField:
            x_set.add(i - e)  # 左边界
            x_set.add(i + e)  # 右边界
            y_set.add(j - e)  # 下边界
            y_set.add(j + e)  # 上边界
        
        # 将收集的边界排序，便于建立坐标到索引的映射
        xs = sorted(x_set)
        ys = sorted(y_set)
        
        # 建立坐标到索引的映射字典，实现离散化（大坐标→小索引）
        x_mapper = {v: i for i, v in enumerate(xs)}
        y_mapper = {v: i for i, v in enumerate(ys)}
        
        # 获取离散化后的维度（边界数量决定网格数）
        n, m = len(xs), len(ys)
        
        # 初始化二维差分数组，大小为(n+2)×(m+2)以避免边界越界
        # 差分数组用于高效对矩形区域进行增减操作
        diff = [[0] * (m + 2) for _ in range(n + 2)]
        
        # 遍历每个力场，更新差分数组
        for i, j, e in forceField:
            # 计算当前力场在离散化后的矩形边界索引
            row1 = x_mapper[i - e]  # 左边界对应的x索引
            col1 = y_mapper[j - e]  # 下边界对应的y索引
            row2 = x_mapper[i + e]  # 右边界对应的x索引
            col2 = y_mapper[j + e]  # 上边界对应的y索引
            
            # 二维差分更新：对矩形区域[row1..row2, col1..col2]整体+1
            diff[row1][col1] += 1
            diff[row1][col2 + 1] -= 1
            diff[row2 + 1][col1] -= 1
            diff[row2 + 1][col2 + 1] += 1
        
        # 利用前缀和还原差分数组，得到每个离散网格点的覆盖次数
        for i in range(n):
            for j in range(m):
                # 二维前缀和公式：当前值 = 自身 + 上方值 + 左方值 - 左上角值
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
        
        # 找到最大覆盖次数，即为答案
        return max(map(max, diff))