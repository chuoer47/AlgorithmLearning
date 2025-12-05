from dataclasses import dataclass
import math
from typing import Optional, Tuple, List


# -----------------------------
# 基础 Point 类
# -----------------------------
@dataclass
class Point:
    x: float
    y: float

    def dist2(self, other: "Point") -> float:
        return (self.x - other.x)**2 + (self.y - other.y)**2

    def dist(self, other: "Point") -> float:
        return math.sqrt(self.dist2(other))


# -----------------------------
# Circle 类，用于外接圆/内切圆
# -----------------------------
@dataclass
class Circle:
    center: Point
    r: float


# -----------------------------
# Triangle 类（核心）
# -----------------------------
@dataclass
class Triangle:
    A: Point
    B: Point
    C: Point

    # --------------------------------
    # 基础几何量
    # --------------------------------
    def area(self) -> float:
        """三角形面积（正负无关）"""
        return abs((self.B.x - self.A.x) * (self.C.y - self.A.y) -
                   (self.C.x - self.A.x) * (self.B.y - self.A.y)) / 2

    def perimeter(self) -> float:
        return self.A.dist(self.B) + self.B.dist(self.C) + self.C.dist(self.A)

    def side_lengths(self) -> Tuple[float, float, float]:
        """返回三边长度 a,b,c，按对边规则：
        a = BC, b = AC, c = AB
        """
        a = self.B.dist(self.C)
        b = self.A.dist(self.C)
        c = self.A.dist(self.B)
        return a, b, c

    # --------------------------------
    # 重心（centroid）
    # --------------------------------
    def centroid(self) -> Point:
        """重心：三条中线的交点"""
        return Point(
            (self.A.x + self.B.x + self.C.x) / 3,
            (self.A.y + self.B.y + self.C.y) / 3
        )

    # --------------------------------
    # 内心（incenter）+ 内切圆
    # --------------------------------
    def incenter(self) -> Point:
        """内心（角平分线交点）"""
        a, b, c = self.side_lengths()
        px = (a * self.A.x + b * self.B.x + c * self.C.x) / (a + b + c)
        py = (a * self.A.y + b * self.B.y + c * self.C.y) / (a + b + c)
        return Point(px, py)

    def inradius(self) -> float:
        """内切圆半径 r"""
        area = self.area()
        s = self.perimeter() / 2
        return area / s

    def incircle(self) -> Circle:
        """返回内切圆"""
        O = self.incenter()
        r = self.inradius()
        return Circle(O, r)

    # --------------------------------
    # 外心（circumcenter）+ 外接圆
    # --------------------------------
    def circumcenter(self) -> Optional[Point]:
        """
        外心：垂直平分线交点
        若三点共线则不存在
        """
        Ax, Ay = self.A.x, self.A.y
        Bx, By = self.B.x, self.B.y
        Cx, Cy = self.C.x, self.C.y

        D = 2 * (Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By))
        if abs(D) < 1e-12:
            return None  # 共线，无法定义外心

        Ux = ((Ax*Ax + Ay*Ay)*(By - Cy) +
              (Bx*Bx + By*By)*(Cy - Ay) +
              (Cx*Cx + Cy*Cy)*(Ay - By)) / D

        Uy = ((Ax*Ax + Ay*Ay)*(Cx - Bx) +
              (Bx*Bx + By*By)*(Ax - Cx) +
              (Cx*Cx + Cy*Cy)*(Bx - Ax)) / D

        return Point(Ux, Uy)

    def circumradius(self) -> Optional[float]:
        """外接圆半径"""
        O = self.circumcenter()
        if O is None:
            return None
        return O.dist(self.A)

    def circumcircle(self) -> Optional[Circle]:
        """返回外接圆（若存在）"""
        O = self.circumcenter()
        if O is None:
            return None
        return Circle(O, O.dist(self.A))

    # --------------------------------
    # 判断点是否在三角形内（含边界）
    # --------------------------------
    def contains_point(self, P: Point) -> bool:
        """采用面积法判断"""
        area_total = self.area()
        area1 = Triangle(P, self.B, self.C).area()
        area2 = Triangle(self.A, P, self.C).area()
        area3 = Triangle(self.A, self.B, P).area()

        return abs((area1 + area2 + area3) - area_total) < 1e-12


# -----------------------------
# main: 用例示范
# -----------------------------
def main():
    A = Point(0, 0)
    B = Point(4, 0)
    C = Point(2, 3)

    tri = Triangle(A, B, C)

    print("Area =", tri.area())
    print("Perimeter =", tri.perimeter())

    print("Centroid =", tri.centroid())

    print("Incenter =", tri.incenter())
    print("Inradius =", tri.inradius())
    print("Incircle =", tri.incircle())

    print("Circumcenter =", tri.circumcenter())
    print("Circumradius =", tri.circumradius())
    print("Circumcircle =", tri.circumcircle())

    P = Point(2, 1)
    print("P in triangle? =", tri.contains_point(P))


if __name__ == "__main__":
    main()
