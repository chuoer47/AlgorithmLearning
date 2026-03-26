"""
https://www.acwing.com/problem/content/378/
"""
visit = set()


def match(x):
    for i, p in enumerate(graph[x]):
        if p != 1 or i in visit:  # 不可以链接到
            continue
        visit.add(i)  # 访问加一下
        if i not in dictMatch:
            dictMatch[i] = x
            return True
        else:
            t = dictMatch[i]
            if match(t):
                dictMatch[i] = x
                return True
    return False


if __name__ == '__main__':
    while True:
        dictMatch = dict()
        # 数据录入还有坑，笑死
        first = input()
        if first[0] == "0":
            break
        n, m, k = map(int, first.strip().split(" "))
        graph = [[0] * (m + 1) for _ in range(n + 1)]
        for _ in range(k):
            i, ai, bi = map(int, input().strip().split(" "))
            if ai == 0 or bi == 0:  # 模式0就不用管了
                continue
            graph[ai][bi] = 1
        ans = 0
        for i in range(1, n + 1):
            if match(i):
                visit = set()  # 清空一下
                ans += 1
        print(ans)
