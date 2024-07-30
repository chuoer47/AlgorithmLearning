"""
https://www.acwing.com/problem/content/1284/

照着抄完了，收获挺多的hhhh
"""

from collections import Counter


class ACTireNode:
    """AC自动机的结点属性存储"""

    def __init__(self, fa):
        self.s = ''  # end结点自身单词
        self.fail_s = []  # fail指针的单词列表
        self.next = dict()  # 多叉树
        self.is_end = False  # 是否为根节点
        self.fail = None  # fail指针
        self.fa: ACTireNode = fa  # 父节点


class ACTire:
    """AC自动机"""

    def __init__(self):
        self.root = ACTireNode(None)

    def tireInsert(self, s):
        """构建Tire字典树，插入方法"""
        cur = self.root
        for i in s:
            if i not in cur.next:  # 没有对应边
                newNode = ACTireNode(cur)
                newNode.s = cur.s + i
                cur.next[i] = newNode
            cur = cur.next[i]
        cur.is_end = True

    def build(self, words: list):
        """构建AC自动机的函数"""
        # 第一步，完成Tire字典树的构建
        for word in words:
            self.tireInsert(word)
        # 第二步，完成fail指针的建立
        # 主要采用层次遍历
        from collections import deque
        q = deque()
        q.append(self.root)
        depth = 0  # 记录层次遍历的当前深度
        while q:
            nowNum = len(q)  # 记录当前层需要遍历的次数
            for _ in range(nowNum):
                cur: ACTireNode = q.popleft()
                if depth == 1:
                    cur.fail = self.root
                elif depth > 1:  # 遍历更深层次的情况
                    cur.fail = self.root  # 先赋值
                    p = cur.fa.fail  # 指向父结点的fail指针
                    last_c = cur.s[-1]  # 先找到最后一个字符
                    while True:
                        if not p:  # 在当前情况下，只有root的fail是None，即为遍历到根节点停止
                            break
                        if last_c in p.next:
                            cur.fail = p.next[last_c]  # 更新一下fail结点
                            if cur.fail.is_end:  # 是一个单词的末尾结点需要存下消息
                                cur.fail_s.append(cur.fail.s)
                            cur.fail_s.extend(cur.fail.fail_s)  # 把fail指向的单词列表存下来
                            break  # 结束
                        p = p.fail
                q.extend(cur.next.values())  # 拓展队列
            depth += 1  # 遍历层数加1

    def match(self, t, cnt: Counter):
        words = set()  # 记录已经匹配的模式字符串
        ans = 0  # 记录答案
        cur = self.root
        idx = 0
        while idx < len(t):
            v = t[idx]
            if v in cur.next:  # 有一条边
                cur = cur.next[v]
                # 开始判断，计算答案，一定要多判断一下
                if cur.is_end:
                    if cur.s not in words:
                        ans += cnt[cur.s]
                        words.add(cur.s)
                for s in cur.fail_s:
                    if s not in words:
                        ans += cnt[s]
                        words.add(s)
                idx += 1
            else:
                while cur and v not in cur.next:
                    cur = cur.fail
                if cur is None:
                    cur = self.root
                    idx += 1
        return ans


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        words = [input() for _ in range(n)]
        cnt = Counter(words)
        msg = input().strip()
        # 使用AC自动机
        acTire = ACTire()
        acTire.build(words)
        ans = acTire.match(msg, cnt)
        print(ans)
