import sys
from copy import deepcopy


class Res:
    def __init__(self, length, flag):
        self.length = length
        self.flag = flag


def dfs(node: str, t: list, dict_word: dict, dict_word_count: dict, res: Res, first: str):
    length = res.length + len(node) - 1
    flag = res.flag
    # 去除t里面的元素
    if len(t) != 0:
        for i in range(0, len(node)):
            if node[i] in t:
                t.remove(node[i])
    # 根据count字典删除dict_word里面的内容,只有当用到2次时才删除
    dict_word_count[node] = dict_word_count[node] + 1
    count = dict_word_count[node]
    if count == 2:
        del_dict = dict_word[node[0]]
        if node in del_dict:
            del_dict.remove(node)
    # 完成了游玩任务
    if len(t) == 0 and node[-1] == first:
        return Res(length, True)
    # 走到死胡同了
    elif node[-1] not in dict_word:
        return Res(length, False)
    # 开始递归
    else:
        arr = dict_word[node[-1]]
        if not arr:
            return Res(length, False)
        for i in range(0, len(arr)):
            sub_res = dfs(arr[i], t.copy(), deepcopy(dict_word), deepcopy(dict_word_count), Res(length, flag), first)
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


def solve(node, t: list, dict_word: dict, dict_word_count: dict) -> int:
    res = dfs(node, t.copy(), deepcopy(dict_word), deepcopy(dict_word_count), Res(0, flag=False), node[0])
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
        arr.append(input().strip())
    t = list(t)
    sys.setrecursionlimit(10000)  # 例如这里设置为十万
    # 创建字典
    dict_word = dict()
    for i in range(0, N):
        if arr[i][0] in dict_word:
            dict_word[arr[i][0]].append(arr[i])
        else:
            dict_word[arr[i][0]] = [arr[i]]
    dict_word_count = dict()
    for i in range(0, N):
        dict_word_count[arr[i]] = 0
    res = []
    for i in range(0, N):
        res.append(solve((arr[i]), t.copy(), deepcopy(dict_word),deepcopy(dict_word_count)))
    for i in range(0, N):
        print(res[i])
