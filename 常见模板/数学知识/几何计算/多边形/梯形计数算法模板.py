"""
【梯形计数算法模板】
适用场景：给定平面直角坐标系中的若干点，统计能构成梯形的数量（梯形定义：仅有一组对边平行的四边形）
核心思路：
1. 梯形 = 有一组对边平行的四边形 - 平行四边形（两组对边都平行）
2. 用「标准化斜率+截距」区分不同直线，统计同斜率下的边组合数（扣除共线情况）得到「一组对边平行的四边形数」
3. 用「中点+斜率」统计平行四边形数量，最终相减得到梯形数
输入格式：points = [[x1,y1], [x2,y2], ..., [xn,yn]]（整数坐标点列表）
输出格式：int（梯形的数量）
"""
from collections import defaultdict
from typing import List
from math import gcd


# ===================== 通用工具函数（无需修改） =====================
def _normalize_slope(p1: tuple, p2: tuple) -> tuple:
    """
    内部工具：计算两点构成直线的标准化斜率（最简分数形式，分母为正）
    - 垂直线（dx=0）：返回 (0, 1) 表示无穷大斜率
    - 水平线（dy=0）：返回 (1, 0) 表示斜率为0
    """
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        return (0, 1)
    if dy == 0:
        return (1, 0)

    # 化简为最简分数，保证分母为正
    g = gcd(abs(dy), abs(dx))
    numerator, denominator = dy // g, dx // g
    if denominator < 0:
        numerator, denominator = -numerator, -denominator

    return (numerator, denominator)


def _get_line_params(p1: tuple, p2: tuple) -> tuple:
    """内部工具：计算直线的(标准化斜率, 标准化截距)，均为最简分数形式"""
    slope = _normalize_slope(p1, p2)
    x1, y1 = p1
    sn, sd = slope

    # 分类型计算截距（垂直线/水平线/普通直线）
    if slope == (0, 1):  # 垂直线
        intercept = (x1, 1)
    elif slope == (1, 0):  # 水平线
        intercept = (y1, 1)
    else:
        # 截距公式：c = y1 - (sn/sd)*x1 = (y1*sd - sn*x1)/sd
        intercept_num = y1 * sd - sn * x1
        intercept_den = sd
        if intercept_num == 0:
            intercept = (0, 1)
        else:
            g = gcd(abs(intercept_num), abs(intercept_den))
            intercept = (intercept_num // g, intercept_den // g)

    return slope, intercept


def _calc_combination_pairs(count_list: List[int]) -> tuple:
    """
    内部工具：预处理组合数
    返回：(总边对数, 共线边对数)
    - 总边对数：C(总边数, 2)
    - 共线边对数：求和 C(单条直线的边数, 2)
    """
    total_edges = sum(count_list)
    total_pairs = total_edges * (total_edges - 1) // 2
    collinear_pairs = sum(e * (e - 1) // 2 for e in count_list)
    return total_pairs, collinear_pairs


def _count_parallelograms(points: List[List[int]]) -> int:
    """内部工具：统计点集中平行四边形的数量（排除共线情况）"""
    n = len(points)
    if n < 4:
        return 0

    # 键：中点(2x,2y)（避免浮点数）；值：{斜率: 该中点+斜率的边数}
    mid_slope_counter = defaultdict(lambda: defaultdict(int))

    for i in range(n):
        p1 = (points[i][0], points[i][1])
        for j in range(i + 1, n):
            p2 = (points[j][0], points[j][1])
            mid = (p1[0] + p2[0], p1[1] + p2[1])
            slope = _normalize_slope(p1, p2)
            mid_slope_counter[mid][slope] += 1

    total = 0
    for mid in mid_slope_counter:
        slope_counts = list(mid_slope_counter[mid].values())
        total_pairs, collinear_pairs = _calc_combination_pairs(slope_counts)
        total += (total_pairs - collinear_pairs)

    return total


# ===================== 核心调用函数（直接使用） =====================
def count_trapezoids(points: List[List[int]]) -> int:
    """
    主函数：统计点集中梯形的数量
    参数：
        points: List[List[int]] - 平面点列表，每个点为[x,y]整数坐标
    返回：
        int - 梯形的数量
    边界条件：点数量<4时返回0
    """
    n = len(points)
    if n < 4:
        return 0

    # 步骤1：统计「同一斜率」下「不同直线」的边数
    slope_line_counter = defaultdict(lambda: defaultdict(int))
    for i in range(n):
        p1 = (points[i][0], points[i][1])
        for j in range(i + 1, n):
            p2 = (points[j][0], points[j][1])
            slope, intercept = _get_line_params(p1, p2)
            slope_line_counter[slope][intercept] += 1

    # 步骤2：计算「有一组对边平行的四边形总数」
    total_parallel_pairs = 0
    for slope in slope_line_counter:
        line_counts = list(slope_line_counter[slope].values())
        total_pairs, collinear_pairs = _calc_combination_pairs(line_counts)
        total_parallel_pairs += (total_pairs - collinear_pairs)

    # 步骤3：扣除平行四边形数量，得到梯形数
    parallelogram_count = _count_parallelograms(points)

    return total_parallel_pairs - parallelogram_count


# ===================== 示例用法（可删除/替换为题目输入） =====================
if __name__ == "__main__":
    # 示例1：基础测试（4个点构成1个梯形，无平行四边形）
    test_points1 = [[0, 0], [0, 1], [1, 0], [2, 1]]
    print(f"示例1梯形数量：{count_trapezoids(test_points1)}")  # 输出：1

    # 示例2：含平行四边形的测试（5个点：1个平行四边形 + 1个梯形 → 最终输出1）
    test_points2 = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0]]
    print(f"示例2梯形数量：{count_trapezoids(test_points2)}")  # 输出：1

    # 示例3：点数量不足4 → 输出0
    test_points3 = [[0, 0], [1, 1], [2, 2]]
    print(f"示例3梯形数量：{count_trapezoids(test_points3)}")  # 输出：0