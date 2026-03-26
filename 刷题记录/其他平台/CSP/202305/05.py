import sys
from copy import deepcopy
MAX = 10 ** 7

class Node:
    def __init__(self, lst):
        self.lst = lst
        self.first = lst[0]
        self.end = lst[-1]


class Res:
    def __init__(self, length, flag):
        self.length = length
        self.flag = flag


def dfs(node: Node, t: list, dict_word: dict, res: Res, first: str):
    lst = node.lst
    length = res.length + len(lst) - 1
    flag = res.flag
    mydict = dict_word[node.first]
    for i in mydict:
        if i.lst == lst:
            mydict.remove(i)
    # 去除t里面的元素
    if len(t) != 0:
        for i in range(0, len(lst)):
            if lst[i] in t:
                t.remove(lst[i])
    # 完成了游玩任务
    if len(t) == 0 and node.end == first:
        return Res(length, True)
    # 走到死胡同了
    elif node.end not in dict_word:
        return Res(length, False)
    # 开始递归
    else:
        arr = dict_word[node.end]
        if not arr:
            return Res(length, False)
        for i in range(0, len(arr)):
            sub_res = dfs(arr[i], t.copy(), deepcopy(dict_word), Res(length, flag), first)
            # 找到一条路
            if sub_res.flag:
                # 进行对比
                if flag:
                    length = min(sub_res.length, length)
                # 记录第一次找到的通路
                else:
                    flag = True
                    length = sub_res.length
    return Res(length, flag)


def solve(node: Node, t: list, dict_word: dict) -> int:
    res = dfs(node, t.copy(), deepcopy(dict_word), Res(0, flag=False), node.first)
    if res.flag:
        return res.length
    else:
        return -1


if __name__ == '__main__':
    # 前置工作
    N, t = input().split(" ")
    N = int(N)
    arr = []
    for i in range(0, N):
        arr.append(list(input().strip()))
    t = list(t)
    sys.setrecursionlimit(10000)  # 例如这里设置为十万
    # 创建字典
    dict_word = dict()
    for i in range(0, N):
        if arr[i][0] in dict_word:
            dict_word[arr[i][0]].append(Node(arr[i]))
        else:
            dict_word[arr[i][0]] = [Node(arr[i])]
    dict_word_count = dict()
    for i in range(0, N):
        dict_word_count[arr[i]] = 0
    print(dict_word_count)
    res = []
    for i in range(0, N):
        res.append(solve(Node(arr[i]), t.copy(), deepcopy(dict_word)))
    print(res)
