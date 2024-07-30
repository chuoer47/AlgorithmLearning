"""
https://www.acwing.com/problem/content/description/100/
纯数学问题，完全想不出来，挺没意思的
不过递归的思想还是体现得太巧妙了
"""


def calXY(level, n):
    """
    level:地图等级
    n:第几个数
    """
    if level == 0:
        return (0, 0)
    pre_level = level - 1
    pre_length = (1 << pre_level)
    pre_area = pre_length * pre_length
    # 根据px,py获得当前的x,y
    px, py = calXY(pre_level, n % pre_area)  # 获得上一个等级的坐标点
    case = n // pre_area
    x, y = px, py
    if case == 0:
        x, y = py, px
    elif case == 1:
        x, y = px, py + pre_length
    elif case == 2:
        x, y = px + pre_length, py + pre_length
    else:
        x, y = 2 * pre_length - py - 1, pre_length - px - 1  # 这里减一忘记了，debug了贼久，烦躁！
    return (x, y)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().strip().split(" "))
        x1, y1 = calXY(n, a - 1)
        x2, y2 = calXY(n, b - 1)
        r1, r2 = 10 * (x1 - x2), 10 * (y1 - y2)
        dis = round((r1 ** 2 + r2 ** 2) ** 0.5) # 四舍五入函数
        print(dis)
