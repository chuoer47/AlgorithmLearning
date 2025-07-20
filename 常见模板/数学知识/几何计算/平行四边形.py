from collections import defaultdict

def find_parallelogram_points(p1, p2, p3):
    """
    给定点p1, p2, p3，求可以构成平行四边形的另外三个点。

    参数:
    p1 (tuple): 第一个点的坐标 (x1, y1)
    p2 (tuple): 第二个点的坐标 (x2, y2)
    p3 (tuple): 第三个点的坐标 (x3, y3)

    返回:
    list: 包含三个点的列表，每个点都是一个元组 (x, y)
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # 计算三种可能的第四个点
    point1 = (x3 + (x1 - x2), y3 + (y1 - y2))
    point2 = (x2 + (x1 - x3), y2 + (y1 - y3))
    point3 = (x1 + (x2 - x3), y1 + (y2 - y3))

    return [point1, point2, point3]

def count_parallelograms(nums):
    """
    计算给定点数组中能构成的平行四边形数目，排除共线点形成的无效情况。

    参数:
    nums (list): 点的数组，每个点表示为 [x, y]

    返回:
    int: 有效平行四边形的数量
    """
    n = len(nums)
    if n < 4:
        return 0

    # 存储每个中点对应的边，按斜率分组
    midpoint_slopes = defaultdict(lambda: defaultdict(int))

    # 计算所有点对的中点和斜率
    for i in range(n):
        x1, y1 = nums[i]
        for j in range(i + 1, n):
            x2, y2 = nums[j]

            # 计算中点 (乘以2避免浮点数)
            mid_x = x1 + x2
            mid_y = y1 + y2
            midpoint = (mid_x, mid_y)

            # 计算斜率 dy/dx，标准化为最简分数
            dx = x2 - x1
            dy = y2 - y1

            if dx == 0:
                # 垂直线，斜率为无穷大，用 (0, 1) 表示
                slope = (0, 1)
            else:
                # 计算最简分数形式的斜率
                g = gcd(abs(dy), abs(dx))
                numerator = dy // g
                denominator = dx // g

                # 确保分母为正，统一方向
                if denominator < 0:
                    numerator = -numerator
                    denominator = -denominator

                slope = (numerator, denominator)

            # 更新对应中点和斜率的边计数
            midpoint_slopes[midpoint][slope] += 1

    # 计算平行四边形数目
    total = 0

    for midpoint in midpoint_slopes:
        slopes = midpoint_slopes[midpoint]
        edges = list(slopes.values())
        sum_edges = sum(edges)

        # 所有可能的边对数目
        total_pairs = sum_edges * (sum_edges - 1) // 2

        # 减去共线的边对数目
        collinear_pairs = sum(e * (e - 1) // 2 for e in edges)

        # 有效平行四边形数目
        valid_pairs = total_pairs - collinear_pairs
        total += valid_pairs

    return total