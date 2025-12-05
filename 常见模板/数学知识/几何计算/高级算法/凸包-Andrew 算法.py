from typing import List, Tuple


class Vec:
    """向量类，提供基本的向量运算"""
    __slots__ = 'x', 'y'

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __sub__(self, b: "Vec") -> "Vec":
        """向量减法"""
        return Vec(self.x - b.x, self.y - b.y)

    def det(self, b: "Vec") -> float:
        """计算两个向量的行列式（相当于叉积）"""
        return self.x * b.y - self.y * b.x

    def dot(self, b: "Vec") -> float:
        """计算两个向量的点积"""
        return self.x * b.x + self.y * b.y

    def to_tuple(self) -> Tuple[float, float]:
        """转换为元组形式"""
        return (self.x, self.y)

    def __eq__(self, other: "Vec") -> bool:
        """判断两个向量是否相等"""
        if not isinstance(other, Vec):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        """用于集合去重的哈希函数"""
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        """用于调试的字符串表示"""
        return f"Vec({self.x}, {self.y})"


class ConvexHull:
    """
    凸包计算类，使用Andrew算法计算平面点集的凸包
    确保在计算上下凸包时排序点集已正确初始化
    """

    def __init__(self, points: List[Tuple[float, float]]):
        """
        初始化凸包计算器

        参数:
            points: 点集列表，每个点是一个包含x和y坐标的元组
        """
        # 将点转换为Vec对象并去重
        self.points = list({Vec(x, y) for x, y in points})
        # 存储计算出的凸包
        self.hull = []
        # 存储排序后的点集
        self.sorted_points = []

    def _ensure_sorted(self):
        """确保点集已排序，若未排序则进行排序（内部辅助方法）"""
        if not self.sorted_points and len(self.points) > 0:
            self.sorted_points = sorted(self.points, key=lambda v: (v.x, v.y))

    def create_lower_hull(self) -> List[Vec]:
        """
        构建下凸包（公开方法）

        返回:
            下凸包点列表（Vec对象）
        """
        # 确保点集已排序
        self._ensure_sorted()

        lower = []
        for p in self.sorted_points:
            # 当最后两个点与当前点形成非左拐时，移除最后一个点
            while len(lower) >= 2 and (lower[-1] - lower[-2]).det(p - lower[-1]) <= 0:
                lower.pop()
            lower.append(p)
        return lower

    def create_upper_hull(self) -> List[Vec]:
        """
        构建上凸包（公开方法）

        返回:
            上凸包点列表（Vec对象）
        """
        # 确保点集已排序
        self._ensure_sorted()

        upper = []
        # 从右到左扫描点
        for p in reversed(self.sorted_points):
            # 当最后两个点与当前点形成非左拐时，移除最后一个点
            while len(upper) >= 2 and (upper[-1] - upper[-2]).det(p - upper[-1]) <= 0:
                upper.pop()
            upper.append(p)
        return upper

    def compute(self) -> List[Tuple[float, float]]:
        """
        计算凸包并返回结果

        返回:
            凸包上的点列表（元组形式），按顺时针方向排列
        """
        # 处理特殊情况
        if len(self.points) <= 1:
            self.hull = [p.to_tuple() for p in self.points]
            return self.hull
        if len(self.points) == 2:
            self.hull = [p.to_tuple() for p in self.points]
            return self.hull

        # 确保点集已排序
        self._ensure_sorted()

        # 分别构建下凸包和上凸包
        lower_hull = self.create_lower_hull()
        upper_hull = self.create_upper_hull()

        # 合并下凸包和上凸包，移除重复点（首尾点相同）
        full_hull = lower_hull[:-1] + upper_hull[:-1]
        # 转换为元组形式返回
        self.hull = [p.to_tuple() for p in full_hull]
        return self.hull

    def get_hull(self) -> List[Tuple[float, float]]:
        """
        获取凸包结果，如果尚未计算则先进行计算

        返回:
            凸包上的点列表（元组形式）
        """
        if not self.hull:
            self.compute()
        return self.hull.copy()

    def get_lower_hull(self) -> List[Tuple[float, float]]:
        """
        获取下凸包结果

        返回:
            下凸包点列表（元组形式）
        """
        lower_hull = self.create_lower_hull()
        return [p.to_tuple() for p in lower_hull]

    def get_upper_hull(self) -> List[Tuple[float, float]]:
        """
        获取上凸包结果

        返回:
            上凸包点列表（元组形式）
        """
        upper_hull = self.create_upper_hull()
        return [p.to_tuple() for p in upper_hull]


# 测试代码
if __name__ == "__main__":
    # 测试案例：直接获取上下凸包（不先调用compute）
    test_points = [(0, 0), (1, 1), (2, 0), (1, -1), (0, 1), (1, 2), (2, 1)]
    hull_calculator = ConvexHull(test_points)

    # 直接获取下凸包（不先调用compute）
    lower_hull = hull_calculator.get_lower_hull()
    print("下凸包点集：", lower_hull)

    # 直接获取上凸包（不先调用compute）
    upper_hull = hull_calculator.get_upper_hull()
    print("上凸包点集：", upper_hull)

    # 获取完整凸包
    full_hull = hull_calculator.get_hull()
    print("完整凸包点集：", full_hull)

    # 测试空点集和单点集情况
    empty_points = []
    empty_hull = ConvexHull(empty_points)
    print("\n空点集凸包：", empty_hull.get_hull())

    single_point = [(5, 5)]
    single_hull = ConvexHull(single_point)
    print("单点集凸包：", single_hull.get_hull())
    print("单点集下凸包：", single_hull.get_lower_hull())
