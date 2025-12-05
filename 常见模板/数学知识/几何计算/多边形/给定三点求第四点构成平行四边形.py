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
