"""
【算法通用直线类】
核心：封装Line类处理直线的标准化、相等判断、哈希；

"""
from math import gcd
from typing import Tuple


class Line:
    """
    算法专用直线类：
    - 支持两点构造直线
    - 标准化斜率/截距（最简分数，分母为正），避免浮点数精度问题
    - 重写__eq__和__hash__，可作为字典键/集合元素
    """

    def __init__(self, p1: Tuple[int, int], p2: Tuple[int, int]):
        """
        构造函数：通过两个整数坐标点初始化直线
        :param p1: 点1，格式 (x1, y1)
        :param p2: 点2，格式 (x2, y2)
        """
        if p1 == p2:
            raise ValueError("两点不能重合，无法构造直线")

        self.x1, self.y1 = p1
        self.x2, self.y2 = p2
        self._normalize()  # 初始化时自动标准化斜率和截距

    def _normalize(self):
        """核心：标准化斜率（slope）和截距（intercept）为最简分数形式"""
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1

        # 1. 标准化斜率（分子num，分母den）
        if dx == 0:  # 垂直线：斜率无穷大，用(0,1)表示
            self.slope_num, self.slope_den = 0, 1
        elif dy == 0:  # 水平线：斜率为0，用(1,0)表示
            self.slope_num, self.slope_den = 1, 0
        else:
            g = gcd(abs(dy), abs(dx))
            self.slope_num = dy // g
            self.slope_den = dx // g
            # 保证分母为正，统一斜率表示
            if self.slope_den < 0:
                self.slope_num = -self.slope_num
                self.slope_den = -self.slope_den

        # 2. 标准化截距（分子num，分母den）
        if self.slope_den == 1 and self.slope_num == 0:  # 垂直线 x = a
            self.intercept_num = self.x1
            self.intercept_den = 1
        elif self.slope_den == 0 and self.slope_num == 1:  # 水平线 y = b
            self.intercept_num = self.y1
            self.intercept_den = 1
        else:  # 普通直线 y = (slope_num/slope_den)x + c
            # 截距公式：c = y1 - (slope_num/slope_den)*x1 = (y1*slope_den - slope_num*x1)/slope_den
            intercept_num = self.y1 * self.slope_den - self.slope_num * self.x1
            intercept_den = self.slope_den

            if intercept_num == 0:
                self.intercept_num, self.intercept_den = 0, 1
            else:
                g = gcd(abs(intercept_num), abs(intercept_den))
                self.intercept_num = intercept_num // g
                self.intercept_den = intercept_den // g

    @property
    def slope(self) -> Tuple[int, int]:
        """返回标准化斜率（分子，分母）"""
        return (self.slope_num, self.slope_den)

    @property
    def intercept(self) -> Tuple[int, int]:
        """返回标准化截距（分子，分母）"""
        return (self.intercept_num, self.intercept_den)

    def __eq__(self, other: "Line") -> bool:
        """判断两条直线是否相等：斜率+截距都相同"""
        if not isinstance(other, Line):
            return False
        return (self.slope == other.slope) and (self.intercept == other.intercept)

    def __hash__(self) -> int:
        """哈希函数：基于斜率和截距的元组，支持作为字典键"""
        return hash((self.slope_num, self.slope_den, self.intercept_num, self.intercept_den))

    def __repr__(self) -> str:
        """打印直线信息（方便调试）"""
        if self.slope == (0, 1):  # 垂直线
            return f"Line(x={self.intercept_num})"
        elif self.slope == (1, 0):  # 水平线
            return f"Line(y={self.intercept_num})"
        else:  # 普通直线
            return f"Line(y=({self.slope_num}/{self.slope_den})x + ({self.intercept_num}/{self.intercept_den}))"
