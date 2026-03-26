"""
https://www.acwing.com/problem/content/345/
"""


def solve():
    nowElement = set()
    for turn, data in enumerate(order):
        x, y = data
        nowElement.add(x)
        nowElement.add(y)
        area[x][y] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    area[i][j] |= area[i][k] & area[k][j]
        # 然后根据图来判断能否找到一个排序，则输出结果；
        # 若找到环，则输出为有矛盾。

        # 第一步，先找环
        for i in range(n):
            for j in range(i, n):
                if area[i][j] == 1 and area[j][i] == 1:
                    return "Inconsistency found after {} relations.".format(turn + 1)

        # 第二步，找关系
        if len(nowElement) < n:  # 剪枝
            continue
        # 根据入度，出度来排序
        in_deg = [0] * n
        out_deg = [sum(area[i]) for i in range(n)]
        for i in range(n):
            for j in range(n):
                if area[j][i]:
                    in_deg[i] += 1
        ans = [-1] * n
        for i in range(n):
            if in_deg[i] + out_deg[i] == n - 1:
                ans[in_deg[i]] = i
            else:
                break
        if -1 not in ans:  # 找到排序结果了
            s = ""
            for i in ans:
                s += chr(i + ord("A"))
            return "Sorted sequence determined after {} relations: {}.".format(turn + 1, s)
    return "Sorted sequence cannot be determined."


if __name__ == '__main__':
    while True:
        n, m = map(int, input().strip().split(" "))
        if n == 0 and m == 0:
            break
        area = [[0] * n for _ in range(n)]
        order = []
        for _ in range(m):
            s = input()
            x, y = ord(s[0]) - ord("A"), ord(s[-1]) - ord("A")
            order.append([x, y])
        print(solve())
