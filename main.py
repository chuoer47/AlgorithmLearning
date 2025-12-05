from collections import defaultdict
from typing import List
from math import gcd


# -------------------------- 预处理通用函数（核心计算逻辑封装） --------------------------
def calculate_combination_count(count_list: List[int]) -> tuple:
    """
    预处理计算：给定一组边数列表，返回(总边对数, 共线边对数)
    总边对数 = C(总边数, 2) = sum(count_list) * (sum(count_list)-1) // 2
    共线边对数 = 求和 C(e, 2) （每个直线内的边数两两组合）
    """
    total_edges = sum(count_list)
    total_pairs = total_edges * (total_edges - 1) // 2  # 所有边的两两组合数
    collinear_pairs = sum(e * (e - 1) // 2 for e in count_list)  # 共线边的两两组合数
    return total_pairs, collinear_pairs


def get_normalized_slope(p1: tuple, p2: tuple) -> tuple:
    """通用函数：计算两点构成直线的标准化斜率（最简分数，分母为正）"""
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:  # 垂直线，斜率用(0,1)表示
        return (0, 1)
    if dy == 0:  # 水平线，斜率用(1,0)表示
        return (1, 0)

    # 化简为最简分数并统一分母为正
    g = gcd(abs(dy), abs(dx))
    numerator, denominator = dy // g, dx // g
    if denominator < 0:
        numerator, denominator = -numerator, -denominator

    return (numerator, denominator)


def get_line_params(p1: tuple, p2: tuple) -> tuple:
    """计算直线的标准化（斜率, 截距），均为最简分数形式"""
    slope = get_normalized_slope(p1, p2)
    x1, y1 = p1
    sn, sd = slope

    # 分类型计算截距
    if slope == (0, 1):  # 垂直线
        intercept = (x1, 1)
    elif slope == (1, 0):  # 水平线
        intercept = (y1, 1)
    else:
        # 截距公式：c = (y1*sd - sn*x1)/sd，化简为最简分数
        intercept_num = y1 * sd - sn * x1
        intercept_den = sd
        if intercept_num == 0:
            intercept = (0, 1)
        else:
            g = gcd(abs(intercept_num), abs(intercept_den))
            intercept = (intercept_num // g, intercept_den // g)

    return slope, intercept


# -------------------------- 业务逻辑函数 --------------------------
def count_parallelograms(points: List[List[int]]) -> int:
    """计算点集中有效平行四边形的数量（排除共线情况）"""
    n = len(points)
    if n < 4:
        return 0

    # 键：中点(2x,2y)（避免浮点数）；值：{斜率: 该中点+斜率的边数}
    mid_slope_count = defaultdict(lambda: defaultdict(int))

    for i in range(n):
        p1 = (points[i][0], points[i][1])
        for j in range(i + 1, n):
            p2 = (points[j][0], points[j][1])
            mid = (p1[0] + p2[0], p1[1] + p2[1])
            slope = get_normalized_slope(p1, p2)
            mid_slope_count[mid][slope] += 1

    total = 0
    for mid in mid_slope_count:
        slope_counts = list(mid_slope_count[mid].values())
        # 调用预处理函数，直接获取总边对数和共线边对数
        total_pairs, collinear_pairs = calculate_combination_count(slope_counts)
        total += (total_pairs - collinear_pairs)

    return total


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """计算点集中梯形的数量（梯形=有一组对边平行 - 平行四边形）"""
        # 1. 统计「同一斜率」下「不同直线」的边数
        slope_line_count = defaultdict(lambda: defaultdict(int))
        n = len(points)
        for i in range(n):
            p1 = (points[i][0], points[i][1])
            for j in range(i + 1, n):
                p2 = (points[j][0], points[j][1])
                slope, intercept = get_line_params(p1, p2)
                slope_line_count[slope][intercept] += 1

        # 2. 计算「有一组对边平行」的图形总数（调用预处理函数）
        total_parallel_pairs = 0
        for slope in slope_line_count:
            line_counts = list(slope_line_count[slope].values())
            total_pairs, collinear_pairs = calculate_combination_count(line_counts)
            total_parallel_pairs += (total_pairs - collinear_pairs)

        # 3. 扣除平行四边形数量，得到梯形数量
        parallelogram_count = count_parallelograms(points)

        return total_parallel_pairs - parallelogram_count