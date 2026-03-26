from dataclasses import dataclass
from typing import Optional
import math


@dataclass
class Point:
    x: float
    y: float

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def dist2(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def dist(self, other):
        return math.sqrt(self.dist2(other))


@dataclass
class Segment:
    p1: Point
    p2: Point

    # --------------------------
    # 基础属性
    # --------------------------
    def length(self) -> float:
        return self.p1.dist(self.p2)

    def length2(self) -> float:
        return self.p1.dist2(self.p2)

    # --------------------------
    # 几何关系判断
    # --------------------------
    def contains_point(self, p: Point) -> bool:
        """
        点 p 是否在线段上（含端点）
        """
        v1 = p - self.p1
        v2 = self.p2 - p
        return abs(v1.cross(v2)) < 1e-12 and v1.dot(v2) >= 0

    def intersects(self, other: "Segment") -> bool:
        """
        两线段是否相交（含端点）
        """

        def orientation(a, b, c):
            return (b - a).cross(c - a)

        a, b = self.p1, self.p2
        c, d = other.p1, other.p2

        o1 = orientation(a, b, c)
        o2 = orientation(a, b, d)
        o3 = orientation(c, d, a)
        o4 = orientation(c, d, b)

        # 一般情况
        if o1 * o2 < 0 and o3 * o4 < 0:
            return True

        # 特殊情况：共线 & 在范围内
        if abs(o1) < 1e-12 and other.contains_point(a): return True
        if abs(o2) < 1e-12 and other.contains_point(b): return True
        if abs(o3) < 1e-12 and self.contains_point(c): return True
        if abs(o4) < 1e-12 and self.contains_point(d): return True

        return False

    # --------------------------
    # 距离计算
    # --------------------------
    def distance_to_point(self, p: Point) -> float:
        """
        点到线段的最短距离
        """
        v = self.p2 - self.p1
        w = p - self.p1
        c1 = w.dot(v)
        if c1 <= 0:
            return p.dist(self.p1)
        c2 = v.dot(v)
        if c2 <= c1:
            return p.dist(self.p2)
        b = c1 / c2
        proj = Point(self.p1.x + b * v.x, self.p1.y + b * v.y)
        return p.dist(proj)

    def distance_to_segment(self, other: "Segment") -> float:
        """
        线段到线段的最短距离
        （若相交则为 0）
        """
        if self.intersects(other):
            return 0.0
        return min(
            self.distance_to_point(other.p1),
            self.distance_to_point(other.p2),
            other.distance_to_point(self.p1),
            other.distance_to_point(self.p2)
        )


# -----------------------------------
# main: 用例示范
# -----------------------------------
def main():
    A = Point(0, 0)
    B = Point(4, 0)
    C = Point(2, 1)
    D = Point(2, -2)

    seg1 = Segment(A, B)
    seg2 = Segment(C, D)

    print("seg1 length =", seg1.length())
    print("seg1 contains C? =", seg1.contains_point(C))  # False

    print("seg1 intersects seg2? =", seg1.intersects(seg2))  # True

    print("distance(C, seg1) =", seg1.distance_to_point(C))

    print("distance(seg1, seg2) =", seg1.distance_to_segment(seg2))


if __name__ == "__main__":
    main()
