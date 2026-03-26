from math import hypot, atan2, sin, cos, sqrt, acos

EPS = 1e-9


def eq(a, b): return abs(a - b) < EPS


class Point:
    """2D Point / Vector。支持所有常用几何操作"""
    __slots__ = ("x", "y")

    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    # ----------------------
    # 基础向量运算
    # ----------------------
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Point(self.x * k, self.y * k)

    def __truediv__(self, k):
        return Point(self.x / k, self.y / k)

    # ----------------------
    # 点积、叉积
    # ----------------------
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    # ----------------------
    # 长度、距离
    # ----------------------
    def length(self):
        return hypot(self.x, self.y)

    def dist(self, other):
        return hypot(self.x - other.x, self.y - other.y)

    # ----------------------
    # 角度、单位向量
    # ----------------------
    def angle(self):
        """向量与 x 轴的夹角"""
        return atan2(self.y, self.x)

    def normalized(self):
        """返回单位向量，不修改自身"""
        l = self.length()
        if l < EPS:
            return Point(0, 0)
        return self / l

    # ----------------------
    # 旋转、投影
    # ----------------------
    def rotate(self, rad):
        """逆时针旋转 rad 弧度"""
        return Point(
            self.x * cos(rad) - self.y * sin(rad),
            self.x * sin(rad) + self.y * cos(rad)
        )

    def projection_on(self, base):
        """将当前向量投影到 base 向量上"""
        base_len2 = base.dot(base)
        if base_len2 < EPS:
            return Point(0, 0)
        return base * (self.dot(base) / base_len2)

    # ----------------------
    # 夹角
    # ----------------------
    def angle_with(self, other):
        """返回两个向量的夹角（弧度）"""
        denom = self.length() * other.length()
        if denom < EPS:
            return 0.0
        cosv = self.dot(other) / denom
        cosv = max(-1.0, min(1.0, cosv))
        return acos(cosv)

    def __repr__(self):
        return f"Point({self.x:.6f}, {self.y:.6f})"


class Line:
    """
    2D 无穷直线，方向用向量 dir 表示。
    用点 + 方向向量表示：p0 + t * dir
    """

    __slots__ = ("p", "dir")

    def __init__(self, p: Point, q: Point):
        """
        输入两个点 p, q 表示直线，方向向量 dir = q - p
        """
        self.p = p
        self.dir = q - p

    # --------------------------
    # 基础功能
    # --------------------------
    def is_parallel(self, other) -> bool:
        """判断是否平行"""
        return eq(self.dir.cross(other.dir), 0)

    def is_same(self, other) -> bool:
        """判断是否同一条直线"""
        if not self.is_parallel(other):
            return False
        # 判断是否共线
        return eq((other.p - self.p).cross(self.dir), 0)

    # --------------------------
    # 两直线交点
    # --------------------------
    def intersection(self, other):
        """
        返回两直线交点；若平行返回 None
        """
        u = self.dir
        v = other.dir
        w = other.p - self.p
        denom = u.cross(v)

        if eq(denom, 0):  # 平行
            return None

        t = w.cross(v) / denom
        return self.p + u * t

    # --------------------------
    # 点到直线距离
    # --------------------------
    def dist_to_point(self, a: Point):
        """
        |(a - p) × dir| / |dir|
        """
        return abs((a - self.p).cross(self.dir)) / self.dir.length()

    # --------------------------
    # 点在直线上的投影
    # --------------------------
    def projection(self, a: Point):
        """
        p + dir * t
        t = ((a - p) · dir) / (dir · dir)
        """
        ap = a - self.p
        base = self.dir.dot(self.dir)
        if eq(base, 0):  # 退化情况
            return self.p
        t = ap.dot(self.dir) / base
        return self.p + self.dir * t

    # --------------------------
    # 标准式 ax + by + c = 0 转成 Line
    # --------------------------
    @staticmethod
    def from_abc(a: float, b: float, c: float):
        """
        由标准式 ax + by + c = 0 构造直线
        """
        if abs(a) < EPS and abs(b) < EPS:
            raise ValueError("Invalid line eq: a=b=0")

        # 找两点
        if abs(b) > EPS:
            p1 = Point(0, -c / b)
            p2 = Point(1, -(a + c) / b)
        else:
            # 垂直线 ax + c = 0
            x = -c / a
            p1 = Point(x, 0)
            p2 = Point(x, 1)

        return Line(p1, p2)

    def __repr__(self):
        return f"Line(Point({self.p.x:.4f},{self.p.y:.4f}), dir=({self.dir.x:.4f},{self.dir.y:.4f}))"


def main():
    print("=== Line Basic Test ===")

    l1 = Line(Point(0, 0), Point(5, 5))
    l2 = Line(Point(0, 5), Point(5, 0))

    print("l1:", l1)
    print("l2:", l2)

    print("Parallel:", l1.is_parallel(l2))
    print("Same Line:", l1.is_same(l2))

    inter = l1.intersection(l2)
    print("Intersection:", inter)

    p = Point(3, 0)
    print("Dist from", p, "to l1:", l1.dist_to_point(p))

    proj = l1.projection(p)
    print("Projection of", p, "on l1:", proj)

    print("\n=== From ax+by+c=0 ===")
    l3 = Line.from_abc(1, -1, 0)  # x - y = 0 => y = x
    print("Line from abc:", l3)
    print("Intersection with l1:", l1.intersection(l3))


if __name__ == "__main__":
    main()
