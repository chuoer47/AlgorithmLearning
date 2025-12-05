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


def main():
    print("=== Point Basic Usage ===")
    a = Point(0, 0)
    b = Point(3, 4)

    print("a:", a)
    print("b:", b)

    print("Add:", a + b)
    print("Sub:", b - a)
    print("Scale:", b * 2)

    print("Dot:", a.dot(b))
    print("Cross:", a.cross(b))

    print("Length of b:", b.length())
    print("Distance a->b:", a.dist(b))

    print("Angle of b:", b.angle())
    print("Normalize b:", b.normalized())

    print("Rotate b by 90°:", b.rotate(3.14159 / 2))

    v = Point(2, 1)
    base = Point(3, 0)
    print("Projection of", v, "on", base, "=", v.projection_on(base))

    print("Angle between v and base:", v.angle_with(base))


if __name__ == "__main__":
    main()
