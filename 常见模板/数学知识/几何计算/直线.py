from math import gcd


def calculate_line_params(p1, p2) -> tuple:
    """
    计算由两点p1和p2构成的直线的斜率和截距，使用分数形式表示。
    保证p1,p2不与x轴或者y轴平行

    参数:
    p1 (tuple): 第一个点的坐标 (x1, y1)
    p2 (tuple): 第二个点的坐标 (x2, y2)

    返回:
    tuple: 包含斜率和截距的元组 ((slope_numerator, slope_denominator), (intercept_numerator, intercept_denominator))
    """
    x1, y1 = p1
    x2, y2 = p2

    # 确保两点不相同
    if x1 == x2 and y1 == y2:
        raise ValueError("两点不能相同")

    # 计算斜率 dy/dx
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        slope = (0, 1)
        intercept = (x1, 1)
        return (slope, intercept)
    elif dy == 0:
        slope = (1, 0)
        intercept = (1, y1)
        return (slope, intercept)

    # 化简斜率为最简分数
    slope_gcd = gcd(abs(dy), abs(dx))
    slope_numerator = dy // slope_gcd
    slope_denominator = dx // slope_gcd

    # 确保分母为正，统一方向
    if slope_denominator < 0:
        slope_numerator = -slope_numerator
        slope_denominator = -slope_denominator

    slope = (slope_numerator, slope_denominator)

    # 计算截距 y = mx + c => c = y - mx
    # 截距 c = (y1 * slope_denominator - slope_numerator * x1) / slope_denominator
    intercept_numerator = y1 * slope_denominator - slope_numerator * x1
    intercept_denominator = slope_denominator

    # 化简截距为最简分数
    if intercept_numerator == 0:
        intercept = (0, 1)
    else:
        intercept_gcd = gcd(abs(intercept_numerator), abs(intercept_denominator))
        intercept = (
            intercept_numerator // intercept_gcd,
            intercept_denominator // intercept_gcd
        )

    return (slope, intercept)
