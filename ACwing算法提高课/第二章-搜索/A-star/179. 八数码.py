"""
https://www.acwing.com/problem/content/181/

参考：https://oi-wiki.org/search/astar/
感觉很容易TLE
操作直接使用列表形式算了
"""


def calHx(s):
    """计算hx的值，返回曼哈顿距离"""
    ans = 0
    for i, v in enumerate(s):
        if v != "x":
            # t = int(v)-1
            t = ord(v) - ord("1")
            ans += abs(i // 3 - t // 3) + abs(i % 3 - t % 3)
    return ans


def findx(s):
    for i, v in enumerate(s):
        if v == "x":
            return i // 3, i % 3


def trans(s, first, second):
    ans = list(s)
    ans[first], ans[second] = ans[second], ans[first]
    return "".join(ans)


# 方向选择
chooses = {
    "u": [-1, 0],
    "d": [1, 0],
    "l": [0, -1],
    "r": [0, 1]
}

from heapq import *


def Astar(begin):
    stack = [
        (calHx(begin) + 0, 0, begin, "")
    ]  # 第一项是hx+gx，第二项是gx, 第三项为当前状态，第四项是到达当前方案的步骤记录
    has = set()
    while stack:
        cost, gx, now, method = heappop(stack)
        if now == "12345678x":
            return method
        has.add(now)
        x, y = findx(now)
        for choose in chooses:
            dx, dy = chooses[choose]
            if 0 <= x + dx <= 2 and 0 <= y + dy <= 2:
                next = trans(now, x * 3 + y, (x + dx) * 3 + y + dy)  # 交换
                if next not in has:
                    heappush(stack,
                             (calHx(next) + gx + 1, gx + 1, next, method + choose)
                             )


if __name__ == '__main__':
    indata = input().strip()
    begin = indata.replace(" ", "")

    # 第一步，求解逆序对
    ss = indata.replace(" ", "")
    ss = ss.replace("x", "")
    nipair = 0
    for i in range(0, 8):
        for j in range(i, 8):
            if ss[i] > ss[j]:
                nipair += 1
    # 第二步，分类讨论
    if nipair % 2:
        print("unsolvable")
    else:
        ans = Astar(begin)
        print(ans)
