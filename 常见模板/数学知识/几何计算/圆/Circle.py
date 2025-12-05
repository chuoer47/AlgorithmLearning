from dataclasses import dataclass
import math
from typing import List, Optional

# -----------------------------
# Basic Point Class
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
# Circle Class
# -----------------------------
@dataclass
class Circle:
    center: Point
    r: float

    # ------------------------------------
    # 基础属性
    # ------------------------------------
    def area(self) -> float:
        return math.pi * self.r * self.r

    def diameter(self) -> float:
        return 2 * self.r

    # ------------------------------------
    # 基础判断
    # ------------------------------------
    def contains_point(self, p: Point) -> bool:
        """点是否在圆内（含边界）"""
        return self.center.dist2(p) <= self.r * self.r + 1e-12

    def on_circle(self, p: Point) -> bool:
        """点是否在圆周上"""
        return abs(self.center.dist(p) - self.r) <= 1e-12

    def intersects_circle(self, other: "Circle") -> bool:
        """两个圆是否相交（含外切、内切）"""
        d = self.center.dist(other.center)
        return abs(self.r - other.r) <= d <= (self.r + other.r)

    # ------------------------------------
    # 距离相关
    # ------------------------------------
    def distance_to_point(self, p: Point) -> float:
        """点到圆的最短距离（点在圆内则为 0）"""
        d = self.center.dist(p)
        return max(0.0, d - self.r)

    def distance_to_circle(self, other: "Circle") -> float:
        """
        圆到圆的最短距离：
        - 若重叠或相交，则为 0
        - 否则返回中心距离 - 两半径
        """
        d = self.center.dist(other.center)
        return max(0.0, d - (self.r + other.r))

    # ------------------------------------
    # 和线的关系
    # ------------------------------------
    def intersects_segment(self, seg: "Segment") -> bool:
        """判断圆与线段是否相交"""
        return seg.distance_to_point(self.center) <= self.r + 1e-12

    # ------------------------------------
    # 求两个圆的交点（0/1/2 个）
    # ------------------------------------
    def intersection_points(self, other: "Circle") -> List[Point]:
        """
        返回两个圆的交点（可能是 0 个、1 个、2 个）
        """
        c1, c2 = self.center, other.center
        d = c1.dist(c2)

        # 无交点（相离 or 包含）
        if d > self.r + other.r + 1e-12:
            return []
        if d < abs(self.r - other.r) - 1e-12:
            return []
        if d == 0 and self.r == other.r:
            # 重合的无限交点，不处理
            return []

        # 计算交点
        a = (self.r**2 - other.r**2 + d*d) / (2*d)
        h2 = self.r**2 - a*a
        if h2 < 0:
            h2 = 0
        h = math.sqrt(h2)

        # 中点
        x0 = c1.x + a * (c2.x - c1.x) / d
        y0 = c1.y + a * (c2.y - c1.y) / d

        # 若只有一个交点
        if h == 0:
            return [Point(x0, y0)]

        # 两个交点
        rx = -(c2.y - c1.y) * (h / d)
        ry = (c2.x - c1.x) * (h / d)

        p1 = Point(x0 + rx, y0 + ry)
        p2 = Point(x0 - rx, y0 - ry)
        return [p1, p2]


# -----------------------------
# Segment - used for round intersection check
# -----------------------------
@dataclass
class Segment:
    p1: Point
    p2: Point

    def distance_to_point(self, p: Point) -> float:
        """点到线段距离"""
        vx = self.p2.x - self.p1.x
        vy = self.p2.y - self.p1.y
        wx = p.x - self.p1.x
        wy = p.y - self.p1.y

        c1 = vx * wx + vy * wy
        if c1 <= 0:
            return p.dist(self.p1)

        c2 = vx * vx + vy * vy
        if c2 <= c1:
            return p.dist(self.p2)

        b = c1 / c2
        proj = Point(self.p1.x + b * vx, self.p1.y + b * vy)
        return p.dist(proj)


# -----------------------------------
# main: 用例示范
# -----------------------------------
def main():
    C1 = Circle(Point(0, 0), 3)
    C2 = Circle(Point(4, 0), 3)
    P = Point(1, 1)
    seg = Segment(Point(-1, 0), Point(1, 0))

    print("Area:", C1.area())
    print("Contains P:", C1.contains_point(P))
    print("Distance(P, C1):", C1.distance_to_point(P))

    print("Circle-Circle intersects:", C1.intersects_circle(C2))

    print("Distance(C1, C2):", C1.distance_to_circle(C2))

    print("Intersection points:")
    for p in C1.intersection_points(C2):
        print(f"({p.x:.3f}, {p.y:.3f})")

    print("Segment intersects circle:", C1.intersects_segment(seg))


if __name__ == "__main__":
    main()
